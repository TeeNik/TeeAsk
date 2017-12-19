from django.db import models
from django.contrib.auth.models import User, UserManager


class Profile(User):
    avatar = models.ImageField(upload_to='media', default='default.png')
    objects = UserManager()

    def __unicode__(self):
        return self.username


class Post(models.Model):
    author = models.ForeignKey(Profile, default=None, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True, auto_now=False)
    title = models.TextField()
    text = models.TextField()
    answers = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class Answer(models.Model):
    author = models.ForeignKey(Profile, default=None, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, default=None, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True, auto_now=False)
    text = models.TextField()
    likes = models.IntegerField(default=0)

    def __unicode__(self):
        return self.text

class Like(models.Model):
    user = models.ForeignKey(Profile, default=None, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, default=None, on_delete=models.CASCADE)
    value = models.IntegerField(default=0)

    def __unicode__(self):
        return str(self.id)

class Tag(models.Model):
    name = models.CharField(max_length=30, default=None)

    def __unicode__(self):
        return self.name





