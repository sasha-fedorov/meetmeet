from django.contrib import admin
from .models import Meetup, MeetupParticipation

# Models registrations
admin.site.register(Meetup)
admin.site.register(MeetupParticipation)
