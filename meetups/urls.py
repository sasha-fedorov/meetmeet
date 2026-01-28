from . import views
from django.urls import path

urlpatterns = [
    path('', views.MeetupsList.as_view(), name='home'),
    path('meetups/<int:pk>/', views.meetup_detail, name="meetup_detail"),
]
