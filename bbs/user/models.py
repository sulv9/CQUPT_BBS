
# 基础模型
from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import User

# 扩展注册
from django.dispatch import receiver
from django.db.models.signals import post_save

# Models
from django.conf import settings




class Account(models.Model):
    """
    Account Model:
        扩展了User对象
        user : django.contrib.auth.models.User
        avatar : 头像ID
        gender : 性别
        signInTime : 注册时间
    """
    # 用户登录和验证的User
    user = models.OneToOneField(
        User, on_delete=models.CASCADE,related_name='Account')
    # 头像
    avatar = models.ImageField(upload_to='avatar')
    # 性别
    gender = models.CharField(max_length=5, verbose_name='Gender')

    def __str__(self) -> str:
        return "%s"%(self.user.username)

class Topic(models.Model):
    """
    Topic Model:
        title : 标题 Chars
        pub_time : 出版时间 Date

    """
    title = models.CharField(max_length=100)
    pub_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title



class Article(models.Model):
    """
    Article Model:
        topic : 类别 外键 Topic Model
        title : 标题 Char Max = 200
        content : 内容 Text
        pub_time : 出版日期
        owner : 作者 外键 Account
"""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    # short = content[:40] + '...'
    pub_time = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(Account, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

@receiver(post_save,sender=User)
def creatAccount(sender,instance,created,**kwargs):
    """
        绑定 Acccount 与 User
    """
    if created:
        Account.objects.create(user=instance)
    else:
        instance.Account.save()
