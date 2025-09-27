from django.shortcuts import render
from datetime import date

from .models import Contratos
from app_adm_usuarios.models import ServidorUser

def home(request):
    contratados = ServidorUser.objects.filter(categoria='CONTRATADO').order_by('nome')

    lista = []

    for contratado in contratados:
        aviso = False
        contratos = contratado.contratos.all()
        for contrato in contratos:            
            if a_vencer(contrato.data_fim) and contrato.ativo==True:
                aviso = True
                break
        dados = {'usuario':contratado, 'aviso':aviso}            
        lista.append(dados)
    context = {
        'contratados':lista,
    }
    return render(request, 'app_adm_temporarios/list_contratados.html', context)

def list_contratos(request):
    contratos = Contratos.objects.all().order_by('usuario__nome', '-data_fim')
    context = {
        'contratos':contratos,
    }
    return render(request, 'app_adm_temporarios/list_contratos.html', context)

# Ultilitário

def a_vencer(data_1, dias=30):
    dias_restantes = (data_1 - date.today()).days
    if dias_restantes < 30:
        return True
    else:
        return False
