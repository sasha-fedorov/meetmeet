from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Meetup


class MeetupsList(generic.ListView):
    queryset = Meetup.objects.all()
    template_name = "meetups/meetup_list.html"
    context_object_name = 'meetups'
    paginate_by = 20


def meetup_detail(request, pk):
    """
    Display an individual :model:`meetups.Meetup`.

    **Context**

    ``meetup``
        An instance of :model:`meetups.Meetup`.

    **Template:**

    :template:`meetups/meetup_detail.html`
    """
    queryset = Meetup.objects.filter()
    meetup = get_object_or_404(queryset, pk=pk)
    return render(request, "meetups/meetup_detail.html", {"meetup": meetup},)
