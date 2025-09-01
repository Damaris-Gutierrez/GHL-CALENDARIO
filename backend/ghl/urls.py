from django.urls import path
from . import views

urlpatterns = [
    path("iniciar-oauth/", views.iniciar_oauth, name="iniciar_oauth"),
    path("callback-oauth/", views.callback_oauth, name="callback_oauth"),
    path("enviar-contacto/", views.enviar_contacto, name="enviar_contacto"),
]