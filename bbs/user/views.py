from django.contrib.auth import authenticate, login
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
# from django.db.models.signals import post_save
# from django.dispatch import receiver
from django.contrib.auth.models import User


# 检查输入函数
def loginCheck(userForm:dict):
    if len(userForm['userName'])>15 or len(userForm['userName'])==0:
        return False
    if len(userForm['passWord'])>30 or len(userForm['passWord'])==0:
        return False
    return True


def loginHTML(request:HttpRequest):
    if request.method == 'GET':
        return render(request,'login.html')

    if request.method =='POST':
        userForm = request.POST.dict()
        if not loginCheck(userForm=userForm):
            # 此处修改成动态界面,暂且忽视
            return HttpResponse('输入表单不正确')

        # 登录逻辑
        if userForm['signFlag']=="Login":
            user = authenticate(request,
                                username=userForm['userName'],
                                password=userForm['passWord'])
            if user is not None:
                login(request,user)
                return redirect('/user')
            else:
                # 不存在用户的处理,暂且忽视
                return HttpResponse('不存在此用户')
        elif request.POST['signFlag'] =="SignUp":
            # 此处应是注册逻辑
            user = User.objects.create_user(
                username = userForm['userName'],
                password = userForm['passWord']
            )
            user.save()
            return redirect('/user')


        # userName = request.POST['username']
        # password = request.POST['password']
        # user = authenticate(request,username=userName,password=password)
        # if user is not None:
        #     login(request,user)
        #     return redirect('/user')
        # else:
        #     return HttpResponse('Not a user')
