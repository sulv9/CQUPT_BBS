from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.



class Account(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='extended')
    gender = models.CharField('')
