from django.db import models

from django import forms


# Create your models here.
class Master(models.Model):
    username = models.CharField(max_length=50)
    role = models.CharField(max_length=20, default="None")
    password = models.CharField(max_length=100, default="123")


class Teacher(models.Model):
    Firstname = models.CharField(max_length=30)
    Lastname = models.CharField(max_length=30)
    Username = models.CharField(max_length=30, default="None", unique=True)
    Password = models.CharField(max_length=100, default="123")
    subjects = models.CharField(max_length=100, default="None")
    grades = models.CharField(max_length=100, default="None")
