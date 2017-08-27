from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .forms import *


def index(request):
    title = 'TeeAsk'
    posts = Post.objects.all()
    return render(request, 'index.html', locals())

def login_page(request):
    title = 'TeeAsk'
    login_form = LoginForm(request.POST or None)
    reg_form = RegistrationForm(request.POST or None)

    print(login_form)
    if request.method == 'POST':
        print ("form is valid or not", login_form.is_valid())
        print(login_form.errors)
        if login_form.is_valid():
            user = authenticate(username=login_form.cleaned_data["username"], password=login_form.cleaned_data["password"])
            #user = authenticate(username="teenik", password="starcraft2")
            print(login_form.cleaned_data)
            if user is not None:
                print(user.email)
                login(request, user)

    if request.method == 'POST' and reg_form.is_valid():
        print(2)
        print(reg_form)
        new_form = reg_form.save()

    return render(request, 'login.html', locals())
