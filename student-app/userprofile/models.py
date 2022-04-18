from pyexpat import model
from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    mobile =  models.CharField(max_length=10)
    qualification = models.CharField(max_length=10)

    def __str__(self):
        return self.user.username