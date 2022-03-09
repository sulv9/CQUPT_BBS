<<<<<<< HEAD

from django.contrib.auth import authenticate,login
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect

def loginHTML(request):
    if request.method == 'GET':
        return render(request,'login.html')
    elif  request.method =='POST':
        userName = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=userName,pass
                            word=password)
        if user is not None:
            login(request,user)
            return redirect('/user')
        else:
            return HttpResponse('Not a user')


# def login(request):
#     if request.method =='GET':
#         return render(request,'login.html')
#     if request.method == 'POST':
#         # print(request.POST['username')
#         print('This is POST')
#         return HttpResponse('post is ok')
=======
from multiprocessing import context
from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.
def userHome(request, user_name):
    user = User.objects.get(username=user_name)
    context = {'user': user}
    return render(request, 'user/user.html', context)
>>>>>>> b78de72eb2f9d273799cec6582fef8fac4235eb9
