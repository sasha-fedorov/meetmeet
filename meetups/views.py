from django import forms
from django.views.generic import DetailView, ListView, DeleteView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from .models import Meetup


class MeetupsListView(ListView):
    queryset = Meetup.objects.all()
    template_name = "meetups/meetup_list.html"
    context_object_name = 'meetups'
    paginate_by = 20


class MeetupDetailView(DetailView):
    model = Meetup
    template_name = "meetups/meetup_detail.html"
    context_object_name = "meetup"


class MeetupFormMixin:
    def get_form(self):
        form = super().get_form()
        if 'start_datetime' in form.fields:
            form.fields['start_datetime'].widget = forms.DateTimeInput(
                attrs={
                    'type': 'datetime-local',
                    'class': 'form-control'
                },
                format='%Y-%m-%dT%H:%M'
            )

            if (hasattr(self, 'object') and self.object and
                    self.object.start_datetime):
                dt_format = self.object.start_datetime.strftime(
                    '%Y-%m-%dT%H:%M')
                form.initial['start_datetime'] = dt_format

        return form

    def form_valid(self, form):
        form.instance.organizer = self.request.user
        return super().form_valid(form)


class MeetupCreateView(MeetupFormMixin, CreateView):
    model = Meetup
    fields = ['title', 'description', 'start_datetime', 'duration_minutes',
              'location_text', 'online_link', 'is_open', 'max_participants']


class MeetupUpdateView(MeetupFormMixin, UpdateView):
    model = Meetup
    fields = ['title', 'description', 'start_datetime', 'duration_minutes',
              'location_text', 'online_link',]


class MeetupDeleteView(DeleteView):
    model = Meetup
    success_url = reverse_lazy('meetup_list')

    # Optional: Ensure only the organizer can delete it
    def get_queryset(self):
        return self.model.objects.filter(organizer=self.request.user)
