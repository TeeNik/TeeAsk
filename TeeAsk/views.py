from django.shortcuts import render
from django.shortcuts import render_to_response

def index(request):
    title = 'TeeAsk'
    return render_to_response('index.html', locals())
