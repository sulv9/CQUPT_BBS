from random import random
from django.contrib.auth import authenticate, login ,logout
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
# from django.db.models.signals import post_save
# from django.dispatch import receiver
from django.contrib.auth.models import User

from .models import Article
import random

# 检查输入函数


def loginCheck(userForm: dict):
    if len(userForm['userName']) > 15 or len(userForm['userName']) == 0:
        return False
    if len(userForm['passWord']) > 30 or len(userForm['passWord']) == 0:
        return False

    # 按理说还应该用正则匹配验证输入是否含特殊字符以免构造任意代码执行
    return True


def loginHTML(request: HttpRequest):
    if request.method == 'POST':
        userForm = request.POST.dict()
        if not loginCheck(userForm=userForm):
            # 此处修改成动态界面,暂且忽视
            return HttpResponse('输入表单不正确')
        # 登录逻辑
        if userForm['signFlag'] == "Login":
            user = authenticate(request,
                                username=userForm['userName'],
                                password=userForm['passWord'])
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                # 不存在用户的处理,暂且忽视
                return HttpResponse('不存在此用户')
        elif request.POST['signFlag'] == "SignUp":
            # 此处应是注册逻辑
            user = User.objects.create_user(
                username=userForm['userName'],
                password=userForm['passWord']
            )
            """
                0. 可爱老鼠
                1. 可爱No嘉然
                2. 原来如此嘉然
                3. 180嘉然
                4. 哭泣嘉然
                5. 聪明蛋嘉然
            """
            imgs = [r"https://s3.bmp.ovh/imgs/2022/03/5524b1bf3e53ec04.jpg",
                    r"https://s3.bmp.ovh/imgs/2022/03/62120fa42489d562.png",
                    r"https://s3.bmp.ovh/imgs/2022/03/013ab8afeaa0a57c.png",
                    r"https://s3.bmp.ovh/imgs/2022/03/67ca7fdeb8ee3e03.png",
                    r"https://s3.bmp.ovh/imgs/2022/03/c57b5e822c5c2048.png",
                    r"https://s3.bmp.ovh/imgs/2022/03/17461a3276e3da3a.png",
                    ]
            user.Account.avatar = random.choice(imgs)
            user.save()
            return redirect('/')
    return HttpResponse('Not Vaild')


def userHome(request, user_id):
    cur_user = User.objects.get(id=user_id)
    account = cur_user.Account
    articles = Article.objects.filter(owner=account)
    context = {'cur_user': cur_user, 'account': account, 'articles': articles}
    return render(request, 'user/user.html', context)

def logOut(request:HttpRequest):
    if request.user.is_authenticated:
        logout(request)
        return redirect('/')
    else:
        return HttpResponse("您的账户并未登录")
