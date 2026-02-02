from django import forms
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import get_object_or_404, redirect
from django.views import View
from django.views.generic import DetailView, ListView, DeleteView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from .models import Meetup, MeetupParticipation


class MeetupsListView(ListView):
    """
    List view for all meetups.
    Authenticated users see their own meetups at the top of the list.
    """
    template_name = "meetups/meetup_list.html"
    context_object_name = 'meetups'
    paginate_by = 12

    def get_queryset(self):
        queryset = Meetup.objects.all()
        if self.request.user.is_authenticated:
            # Manually sort to show user's organized events first
            my_meetups = queryset.filter(organizer=self.request.user)
            other_meetups = queryset.exclude(organizer=self.request.user)
            return list(my_meetups) + list(other_meetups)

        return queryset


class MeetupDetailView(DetailView):
    """
    Detailed view for a single meetup.
    Optimized with prefetch_related and includes participation context.
    """
    model = Meetup
    template_name = "meetups/meetup_detail.html"
    context_object_name = "meetup"

    def get_queryset(self):
        # Prefetch users in participation to avoid N+1 query issues
        return super().get_queryset().prefetch_related('participations__user')

    def get_context_data(self, **kwargs):
        """Inject current user's participation status into the template."""
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context['user_participation'] = MeetupParticipation.objects.filter(
                meetup=self.object, user=self.request.user
            ).first()
        return context


class MeetupFormMixin(LoginRequiredMixin):
    """
    Utility mixin to handle common form logic for Create/Update views.
    Adjusts the start_datetime widget for HTML5 datetime compatibility.
    """

    def get_form(self):
        form = super().get_form()
        if 'start_datetime' in form.fields:
            # Use 'datetime-local' input type for better browser support
            form.fields['start_datetime'].widget = forms.DateTimeInput(
                attrs={
                    'type': 'datetime-local',
                    'class': 'form-control'
                },
                format='%Y-%m-%dT%H:%M'
            )

            # Ensure existing date is formatted correctly
            if (hasattr(self, 'object') and self.object and
                    self.object.start_datetime):
                dt_format = self.object.start_datetime.strftime(
                    '%Y-%m-%dT%H:%M')
                form.initial['start_datetime'] = dt_format

        return form

    def form_valid(self, form):
        """Automatically set the current user as the meetup organizer."""
        form.instance.organizer = self.request.user
        return super().form_valid(form)


class MeetupCreateView(MeetupFormMixin, CreateView):
    """View to handle the creation of a new Meetup."""
    model = Meetup
    fields = ['title', 'description', 'start_datetime', 'duration_minutes',
              'location_text', 'online_link', 'is_open', 'max_participants']


class MeetupUpdateView(MeetupFormMixin, UserPassesTestMixin, UpdateView):
    """View to handle editing an existing Meetup (Organizer only)."""
    model = Meetup
    fields = ['title', 'description', 'start_datetime', 'duration_minutes',
              'location_text', 'online_link',]

    def test_func(self):
        """Verify the logged-in user is the actual organizer."""
        obj = self.get_object()
        return obj.organizer == self.request.user

    def handle_no_permission(self):
        """Redirect unauthorized users back to the list."""
        return redirect('meetup_list')


class MeetupDeleteView(DeleteView):
    """View to handle meetup deletion."""
    model = Meetup
    success_url = reverse_lazy('meetup_list')

    def get_queryset(self):
        """Ensure users can only delete meetups they organized."""
        return self.model.objects.filter(organizer=self.request.user)


class ToggleParticipationView(LoginRequiredMixin, View):
    """
    A POST-only view that handles joining or leaving a meetup.
    Creates or deletes MeetupParticipation records.
    """

    def post(self, request, pk):
        meetup = get_object_or_404(Meetup, pk=pk)

        # Organizer check
        if meetup.organizer == request.user:
            messages.warning(request, "You are the organizer.")
            return redirect('meetup_detail', pk=pk)

        participation = MeetupParticipation.objects.filter(
            user=request.user, meetup=meetup
        ).first()

        if participation:
            # If user is already "Going" or "Pending", toggle means "Leave"
            if participation.status in [MeetupParticipation.Status.GOING,
                                        MeetupParticipation.Status.PENDING]:
                participation.delete()
                messages.info(
                    request, "Your request or attendance has been cancelled.")
            else:
                # Re-joining logic for someone who was previously "Not Going"
                participation.status = (
                    MeetupParticipation.Status.GOING
                    if meetup.is_open
                    else MeetupParticipation.Status.PENDING
                )
                participation.save()
        else:
            # Initial join/request logic
            status = (
                MeetupParticipation.Status.GOING
                if meetup.is_open
                else MeetupParticipation.Status.PENDING
            )
            MeetupParticipation.objects.create(
                user=request.user, meetup=meetup, status=status)
            messages.success(
                request, "Success! You've joined or requested to join.")

        return redirect('meetup_detail', pk=pk)


@login_required
def approve_participation(request, pk):
    """Function-based view for organizers to approve requests."""
    participation = get_object_or_404(MeetupParticipation, pk=pk)

    # Security check: Only the organizer of the meetup can approve
    if participation.meetup.organizer == request.user:
        participation.approve()
        messages.success(
            request, f"Approved {participation.user.username}'s request.")
    else:
        messages.error(
            request, "You are not authorized to perform this action.")

    return redirect('meetup_detail', pk=participation.meetup.pk)


@login_required
def reject_participation(request, pk):
    """Function-based view for organizers to reject requests."""
    participation = get_object_or_404(MeetupParticipation, pk=pk)

    if participation.meetup.organizer == request.user:
        participation.reject()
        messages.info(
            request, f"Rejected {participation.user.username}'s request.")
    else:
        messages.error(
            request, "You are not authorized to perform this action.")

    return redirect('meetup_detail', pk=participation.meetup.pk)
