from operator import mod
from tkinter import CASCADE
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

class Account(models.Model):
    user = models.OneToOneField(User, on_delete=CASCADE, related_name='extension')
    avatar = models.IntegerField()