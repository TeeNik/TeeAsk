from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import *


def index(request):
    title = 'TeeAsk'
    posts = Post.objects.all()
    likes = Like.objects.filter(user=request.user).values_list("post")
    print(likes[0][0])
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

def like(request):
    id = request.GET['id']
    value = request.GET['value']
    new_like, created = Like.objects.get_or_create(user=request.user, post=Post.objects.get(id=id))
    post = Post.objects.get(id=id)
    if not created:
        print('already created')
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
        print('create new')
        new_like.value = value
        new_like.save()
        post.likes += int(value)
        post.save()
    likes_count = post.likes
    return HttpResponse(likes_count)

