from django.urls import path

from . import views

urlpatterns = [
    path("home", views.home, name="index_temporarios"),
    path("contatos", views.list_contratos, name="list_contratos"),
    
]