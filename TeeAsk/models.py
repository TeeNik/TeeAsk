from django.db import models

class Users(models.Model):
    username = models.CharField(max_length=25)
    email = models.EmailField()
