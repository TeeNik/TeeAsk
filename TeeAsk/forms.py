from django import forms
from .models import *


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["email", "username", "password"]


class LoginForm(forms.Form):
    username = forms.CharField(label='usrbnm')
    password = forms.CharField(label='pswrd', widget=forms.PasswordInput)

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'text']


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['text']

class AvatarForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar']
