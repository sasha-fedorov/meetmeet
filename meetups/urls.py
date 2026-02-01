from . import views
from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.MeetupsListView.as_view(), name='meetup_list'),
    path('meetups/<int:pk>/',
         views.MeetupDetailView.as_view(), name="meetup_detail"),
    path('meetups/create/',
         views.MeetupCreateView.as_view(), name='meetup_create'),
    path('meetups/<int:pk>/edit/',
         views.MeetupUpdateView.as_view(), name='meetup_update'),
    path('meetups/<int:pk>/delete/',
         views.MeetupDeleteView.as_view(), name='meetup_delete'),
    path('about/', TemplateView.as_view(template_name='about.html'),
         name='about'),
]
