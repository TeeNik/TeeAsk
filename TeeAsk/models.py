from django.db import models
from django.contrib.auth.models import User, UserManager
from taggit.managers import TaggableManager


class Profile(User):
    avatar = models.ImageField(default='default.png')
    objects = UserManager()

    def __unicode__(self):
        return self.username


class Post(models.Model):
    author = models.ForeignKey(Profile, default=None)
    date = models.DateTimeField(auto_now_add=True, auto_now=False)
    title = models.TextField()
    text = models.TextField()
    answers = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    tags = TaggableManager()

    def __str__(self):
        return self.title


class Answer(models.Model):
    author = models.ForeignKey(Profile, default=None)
    post = models.ForeignKey(Post, default=None)
    date = models.DateTimeField(auto_now_add=True, auto_now=False)
    text = models.TextField()
    likes = models.IntegerField()

    def __unicode__(self):
        return self.text

class Like(models.Model):
    user = models.ForeignKey(Profile, default=None)
    post = models.ForeignKey(Post, default=None)
    value = models.IntegerField(default=0)

    def __unicode__(self):
        return str(self.id)

class Tag(models.Model):
    name = models.CharField(max_length=30, default=None)

    def __unicode__(self):
        return self.name





