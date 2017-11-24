from django.contrib.auth.decorators import login_required
import json

from django.core import serializers
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views import View

from .forms import *

class IndexView(View):
    def get(self, request):
        title = 'TeeAsk'

        id = request.GET.get('id')
        posts = None
        if id is not None:
            post = Post.objects.get(id=id)
            posts = Post.objects.filter(author=post.author)
            return render(request, 'index.html', locals())
        else:
            posts = Post.objects.all()
            return render(request, 'index.html', locals())


class LoginView(View):
    def get(self, request):
        title = 'TeeAsk'
        login_form = LoginForm(request.POST or None)
        reg_form = RegistrationForm(request.POST or None)

        if request.method == 'POST':
            if 'log' in request.POST:
                if login_form.is_valid():
                    print(1)
                    user = authenticate(username=login_form.cleaned_data["username"],
                                        password=login_form.cleaned_data["password"])
                    if user is not None:
                        login(request, user)
                        return redirect('/', user)
            else:
                if reg_form.is_valid():
                    print(2)
                    user = Profile.objects.create(email=reg_form.cleaned_data["email"],
                                                  username=reg_form.cleaned_data["username"],
                                                  password=reg_form.cleaned_data["password"])
                    user.save()

                    user = authenticate(username=reg_form.cleaned_data["username"],
                                        password=reg_form.cleaned_data["password"])
                    if user is not None:
                        login(request, user)
                        return redirect('/', user)

        return render(request, 'login.html', locals())

class SettingsView(View):
    def get(self, request):
        title = 'TeeAsk'
        reg_form = RegistrationForm(request.POST or None)

        if request.method == 'POST':
            if reg_form.is_valid():
                print(2)
                user = Profile.objects.create(email=reg_form.cleaned_data["email"],
                                              username=reg_form.cleaned_data["username"],
                                              password=reg_form.cleaned_data["password"])
                user.save()

                user = authenticate(username=reg_form.cleaned_data["username"],
                                    password=reg_form.cleaned_data["password"])

                if user is not None:
                    login(request, user)
                    return redirect('/', user)

        return render(request, 'setting.html', locals())

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('/', {})

class QuestionView(View):
    def get(self, request):
        post_id = request.GET.get('post_id')
        post = Post.objects.get(id=post_id)

        answer_form = AnswerForm(request.POST or None)

        try:
            answers = Answer.objects.filter(post=post)
        except Answer.DoesNotExist:
            answers = None

        if request.method == 'POST':
            if answer_form.is_valid():
                answer = Answer.objects.create(author=request.user, post=post)
                answer.text = answer_form.cleaned_data['text']
                answer.save()
            else:
                print(answer_form.errors)
                print('en')

        return render(request, 'question.html', locals())

class NewQuestionView(View):
    def get(self, request):
        print('HERE')

        ques_form = QuestionForm(initial={'title': 'Заголовок', 'text': 'Текст'})
        if request.user is None:
            return redirect('/', {})

        if request.method == 'POST':
            print(2)
            title = request.POST.get('title')
            text = request.POST.get('text')
            post = Post.objects.create(author=Profile.objects.get(username=request.user))
            post.title = title
            post.text = text
            post.save()
            return redirect('/', request.user)

        return render(request, 'new_question.html', locals())


class LiveView(View):
    def get(self, request):
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
        ctx = {'id': id, 'like': likes_count}
        return HttpResponse(json.dumps(ctx), content_type='application/json')
