from django.contrib.auth.decorators import login_required
import json

from django.core import serializers
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import *


def index(request):
    title = 'TeeAsk'

    id = request.GET.get('id')
    posts = None
    if id is not None:
        post = Post.objects.get(id=id)
        posts = Post.objects.filter(author=post.author)
        #data = serializers.serialize('json', posts);
        #return HttpResponse(data, content_type="application/json")
        return render(request, 'index.html', locals())
    else:
        posts = Post.objects.all()
        return render(request, 'index.html', locals())
    #likes = Like.objects.filter(user=request.user).values_list('post')
    #print(likes[0][0])


def login_page(request):
    title = 'TeeAsk'
    login_form = LoginForm(request.POST or None)
    reg_form = RegistrationForm(request.POST or None)

    if request.method == 'POST':
        if login_form.is_valid():
            user = authenticate(username=login_form.cleaned_data["username"], password=login_form.cleaned_data["password"])
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

def new_question(request):
    ques_form = QuestionForm(request.POST or None)
    if request.user is None:
        return redirect('/', {})

    if request.method == 'POST':
        if ques_form.is_valid():
            data = ques_form.cleaned_data
            post = Post.objects.create(author=Profile.objects.get(username=request.user))
            post.title = data['title']
            post.text = data['text']
            post.save()


    return render(request, 'new_question.html', locals())


def like(request):
    id = request.GET['id']
    value = request.GET['value']
    new_like, created = Like.objects.get_or_create(user=request.user, post=Post.objects.get(id=id))
    post = Post.objects.get(id=id)
    if not created:
        like = Like.objects.get(user=request.user, post=post)
        if int(like.value) != int(value):
            if int(value) > 0:
                post.likes += 2
            else:
                post.likes -= 2
            like.value = value
            like.save()
            post.save()
    else:
        new_like.value = value
        new_like.save()
        post.likes += int(value)
        post.save()
    likes_count = post.likes
    ctx = {'id':id, 'like':likes_count}
    return HttpResponse(json.dumps(ctx), content_type='application/json')

