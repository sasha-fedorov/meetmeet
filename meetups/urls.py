from . import views
from django.urls import path

urlpatterns = [
    path('', views.MeetupsListView.as_view(), name='meetup_list'),
    path('meetups/<int:pk>/',
         views.MeetupDetailView.as_view(), name="meetup_detail"),
    path('meetups/create/',
         views.MeetupCreateView.as_view(), name='meetup_create'),
    path('meetups/<int:pk>/edit/',
         views.MeetupUpdateView.as_view(), name='meetup_update'),
]
