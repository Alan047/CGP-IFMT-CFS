from django.shortcuts import render

def home(request):
    return render(request, 'home.html', context={"msg":"hello"})

def list_servidores(request):
    return render(request, 'app_adm_usuarios/list_servidores.html')
