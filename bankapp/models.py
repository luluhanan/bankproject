from django.db import models
from django.contrib.auth.models import AbstractBaseUser, UserManager
# Create your models here.



class Myform(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    email=models.EmailField()