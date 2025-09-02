from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("ghl/", include("ghl.urls")),  # Prefijo para todos los endpoints GHL
]
