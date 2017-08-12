from django.shortcuts import render
from django.shortcuts import render_to_response
from .forms import *


def index(request):
    title = 'TeeAsk'
    form = RegistrationForm(request.POST or None)
    return render_to_response('index.html', locals())
