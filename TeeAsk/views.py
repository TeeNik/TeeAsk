from django.shortcuts import render
from django.shortcuts import render_to_response
from .forms import *


def index(request):
    title = 'TeeAsk'
    form = RegistrationForm(request.POST or None)
    return render_to_response('index.html', locals())

def login(request):
    title = 'TeeAsk'
    login_form = LoginForm(request.POST or None)
    reg_form = RegistrationForm(request.POST or None)

    if request.method == 'POST' and login_form.is_valid():
        print(login_form)

    if request.method == 'POST' and reg_form.is_valid():
        print(reg_form)

    return  render_to_response('login.html', locals())
