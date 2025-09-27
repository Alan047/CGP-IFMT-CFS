from datetime import date
from dateutil.relativedelta import relativedelta
from django.db import models
from django.conf import settings

class Contratos(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='contratos')
    observacao = models.CharField(max_length=50, blank=True, null=True)
    data_inicio = models.DateField()
    data_fim = models.DateField()
    aviso = models.BooleanField(default=False)
    ativo = models.BooleanField(default=True)


        
    def __str__(self):
        return f'Contrato:{self.usuario} - {self.observacao}'
    
class Estagio(models.Model):
    pass
