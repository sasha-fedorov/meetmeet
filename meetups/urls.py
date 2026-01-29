from . import views
from django.urls import path

urlpatterns = [
    path('', views.MeetupsListView.as_view(), name='meetup_list'),
    path('meetups/<int:pk>/', views.MeetupDetailView.as_view(), name="meetup_detail"),
]
