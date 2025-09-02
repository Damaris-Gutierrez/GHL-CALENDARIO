from django.urls import path
from . import views

urlpatterns = [
    path("ping/", views.ping, name="ping"),
    path("calendars/", views.calendars, name="calendars"),
    path("calendars/<str:calendar_id>/", views.calendar_detail, name="calendar_detail"),
]
