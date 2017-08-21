from django import forms
from .models import *

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ["avatar"]

class LoginForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['username', 'avatar']