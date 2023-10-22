from django.db import models

from django import forms


# Create your models here.
class Master(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    role = models.CharField(max_length=20, default="None")


class Teachers(models.Model):
    Firstname = models.CharField(max_length=30)
    Lastname = models.CharField(max_length=30)
    Username = models.CharField(max_length=30)
    Password = forms.CharField(widget=forms.PasswordInput)
