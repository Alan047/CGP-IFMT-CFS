from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="index"),
    path("servidores/", views.list_servidores, name="list_servidores"),
]