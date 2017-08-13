from django.shortcuts import render
from .forms import *


def index(request):
    title = 'TeeAsk'
    posts = Post.objects.all()
    return render(request, 'index.html', locals())

def login(request):
    title = 'TeeAsk'
    login_form = LoginForm(request.POST or None)
    reg_form = RegistrationForm(request.POST or None)

    if request.method == 'POST' and login_form.is_valid():
        print(1)
        print(login_form)

    if request.method == 'POST' and reg_form.is_valid():
        print(2)
        print(reg_form)
        new_form = reg_form.save()


    return render(request, 'login.html', locals())
