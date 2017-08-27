from django import forms
from .models import *

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["email", "username", "password"]

class LoginForm(forms.Form):
    username = forms.CharField(label='Nombre de usuario')
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput)