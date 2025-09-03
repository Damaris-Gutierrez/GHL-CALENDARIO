from django.urls import path, include

urlpatterns = [
    path("ghl/", include("ghl.urls")),
]
