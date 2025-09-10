# usuarios/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import ServidorUser
from .forms import ServidorUserCreationForm, ServidorUserChangeForm

class ServidorUserAdmin(BaseUserAdmin):
    form = ServidorUserChangeForm
    add_form = ServidorUserCreationForm

    list_display = ('matricula', 'nome', 'categoria','data_ent_exercicio' , 'is_staff')
    list_filter = ('is_staff', 'is_superuser', 'is_active')
    ordering = ('matricula',)

    fieldsets = (
        (None, {'fields': ('matricula', 'password')}),
        ('Informações pessoais', {'fields': ('nome', 'categoria', 'data_ent_exercicio')}),
        ('Permissões', {'fields': ('is_staff', 'is_superuser', 'is_active', 'groups', 'user_permissions')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('matricula', 'nome', 'categoria', 'password1', 'password2', 'is_staff', 'is_superuser')}
        ),
    )

admin.site.register(ServidorUser, ServidorUserAdmin)




   
    
