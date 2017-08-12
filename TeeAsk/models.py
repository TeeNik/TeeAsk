from django.db import models

class User(models.Model):
    username = models.CharField(max_length=25)
    password = models.CharField(max_length=25)
    email = models.EmailField()
    avatar = models.ImageField()

    def __str__(self):
        return self.username

