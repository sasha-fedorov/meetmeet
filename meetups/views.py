from django.views.generic import DetailView, ListView
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
