from django import forms
from .models import *

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        exclude = ["avatar"]

class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        exclude = ['username', 'avatar']