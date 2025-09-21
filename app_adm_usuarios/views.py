from django.shortcuts import render
from .models import ServidorUser
from django.conf import settings

def home(request):
    return render(request, 'home.html', context={"msg":"hello"})

def list_servidores(request):
    usuarios = ServidorUser.objects.all()
    context = {
        'servidores':usuarios,
    }
    return render(request, 'app_adm_usuarios/list_servidores.html', context)
