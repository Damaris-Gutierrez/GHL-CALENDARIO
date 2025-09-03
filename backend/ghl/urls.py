# ghl/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("ping/", views.ping, name="ghl_ping"),
    path("calendars/", views.calendars, name="ghl_calendars"),
    path("calendars/<str:calendar_id>/", views.calendar_detail, name="ghl_calendar_detail"),
]
