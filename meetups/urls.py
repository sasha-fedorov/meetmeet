from . import views
from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    # General List and Detail
    path('', views.MeetupsListView.as_view(), name='meetup_list'),
    path('meetups/<int:pk>/',
         views.MeetupDetailView.as_view(), name="meetup_detail"),

    # Meetup Management (CRUD)
    path('meetups/create/',
         views.MeetupCreateView.as_view(), name='meetup_create'),
    path('meetups/<int:pk>/edit/',
         views.MeetupUpdateView.as_view(), name='meetup_update'),
    path('meetups/<int:pk>/delete/',
         views.MeetupDeleteView.as_view(), name='meetup_delete'),

    # Participation Management
    path('meetup/<int:pk>/toggle-participation/',
         views.ToggleParticipationView.as_view(), name='toggle_participation'),
    path('participation/<int:pk>/approve/',
         views.approve_participation, name='approve_participation'),
    path('participation/<int:pk>/reject/',
         views.reject_participation, name='reject_participation'),

    # Static Pages
    path('about/', TemplateView.as_view(template_name='about.html'),
         name='about'),
]
