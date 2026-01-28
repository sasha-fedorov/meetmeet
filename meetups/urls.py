from . import views
from django.urls import path

urlpatterns = [
    path('', views.MeetupsList.as_view(), name='home'),
]
