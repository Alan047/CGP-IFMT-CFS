from django.urls import path

from . import views

urlpatterns = [
    path("home", views.home, name="index_temporarios"),
    path("contatos", views.list_contratos, name="list_contratos"),
    path("estagiarios", views.list_estagiarios, name="list_estagiarios"),
    
]