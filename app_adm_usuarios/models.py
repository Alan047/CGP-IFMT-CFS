from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class ServidorUserManager(BaseUserManager):
    def create_user(self, matricula, password=None, **extra_fields):
        if not matricula:
            raise ValueError("O usuário precisa ter uma matrícula")
        user = self.model(matricula=matricula, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, matricula, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(matricula, password, **extra_fields)

class ServidorUser(AbstractBaseUser, PermissionsMixin):
    matricula = models.IntegerField(unique=True, null=False, blank=False)
    nome =models.CharField(max_length=100, null=False, blank=False)
    CATEGORIA_CHOICE = [
        ('TAE', 'TAE'),
        ('DOCENTE', 'Docente'),
        ('CONTRATADO', 'Contratado'),
        ('ESTAGIARIO', 'Estagiario')]
    categoria = models.CharField(max_length=20, choices=CATEGORIA_CHOICE, null=True, blank=True)
    data_ent_exercicio = models.DateField(null=True, blank=True)
    estabilidade = models.BooleanField(default=False)
    ativo = models.BooleanField(default=True)
    
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = ServidorUserManager()

    USERNAME_FIELD = 'matricula'   # <- login será pela matrícula
    REQUIRED_FIELDS = ['nome',]

    def __str__(self):
        return f'{self.nome}({self.matricula})'