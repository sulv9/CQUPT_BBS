<<<<<<< HEAD
from urllib.request import AbstractDigestAuthHandler
from xml.dom.pulldom import SAX2DOM
=======
from operator import mod
from tkinter import CASCADE
>>>>>>> b78de72eb2f9d273799cec6582fef8fac4235eb9
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Topic(models.Model):
    title = models.CharField(max_length=100)
    pub_time = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return self.title

class Article(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    short = content[:40] + '...'
    pub_time = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def _str_(self):
        return self.title

<<<<<<< HEAD

class Account(models.Model):
    user =  models.OneToOneField(User,on_delete=models.CASCADE,related_name="extends")
    gender = models.CharField(max_length=10,verbose_name="性别")
=======
class Account(models.Model):
    user = models.OneToOneField(User, on_delete=CASCADE, related_name='extension')
    avatar = models.IntegerField()
>>>>>>> b78de72eb2f9d273799cec6582fef8fac4235eb9
