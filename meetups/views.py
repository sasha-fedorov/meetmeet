from django.shortcuts import render
from django.views import generic
from .models import Meetup


class MeetupsList(generic.ListView):
    queryset = Meetup.objects.all()
    template_name = "meetups/index.html"
    context_object_name = 'meetups'
    paginate_by = 20
