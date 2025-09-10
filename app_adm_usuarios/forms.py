# usuarios/forms.py
from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from .models import ServidorUser

class ServidorUserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Senha', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmação de senha teste', widget=forms.PasswordInput)

    class Meta:
        model = ServidorUser
        fields = ('matricula', 'nome', 'categoria', 'data_ent_exercicio')

    def clean_password2(self):
        # Verifica se as senhas coincidem
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("As senhas não coincidem")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

# usuarios/forms.py
class ServidorUserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField(label="Senha")

    class Meta:
        model = ServidorUser
        fields = ('matricula', 'nome', 'categoria', 'data_ent_exercicio', 'password', 'is_active', 'is_staff')
