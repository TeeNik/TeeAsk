from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import *


def index(request):
    title = 'TeeAsk'
    posts = Post.objects.all()
    return render(request, 'index.html', locals())

def login_page(request):
    title = 'TeeAsk'
    login_form = LoginForm(request.POST or None)
    reg_form = RegistrationForm(request.POST or None)

    if request.method == 'POST':
        if login_form.is_valid():
            user = authenticate(username=login_form.cleaned_data["username"], password=login_form.cleaned_data["password"])
            #user = authenticate(username="teenik", password="starcraft2")
            if user is not None:
                login(request, user)
                return redirect('/', user)

    if request.method == 'POST' and reg_form.is_valid():
        print(2)
        print(reg_form)
        new_form = reg_form.save()

    return render(request, 'login.html', locals())

def logout_page(request):
    logout(request)
    return redirect('/', {})
