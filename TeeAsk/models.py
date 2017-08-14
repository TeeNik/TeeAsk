from django.db import models

class User(models.Model):
    username = models.CharField(max_length=25)
    password = models.CharField(max_length=25)
    email = models.EmailField()
    avatar = models.ImageField()

    def __str__(self):
        return self.username


class Post(models.Model):
    author = models.ForeignKey(User, default=None)
    date = models.DateTimeField(auto_now_add=True, auto_now=False)
    title = models.TextField()
    text = models.TextField()
    answers = models.IntegerField()
    likes = models.IntegerField()

    def __str__(self):
        return self.title


class Answer(models.Model):
    author = models.ForeignKey(User, default=None)
    date = models.DateTimeField(auto_now_add=True, auto_now=False)
    text = models.TextField()
    likes = models.IntegerField()

    def __str__(self):
        return self.text

class Like(models.Model):
    user = models.ForeignKey(User, default=None)
    value = models.IntegerField(default=0)

    def __str__(self):
        return self.user

class Tag(models.Model):
    name = models.CharField(max_length=30, default=None)

    def __str__(self):
        return self.name





