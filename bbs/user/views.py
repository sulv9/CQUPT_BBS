from multiprocessing import context
from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.
def userHome(request, user_name):
    user = User.objects.get(username=user_name)
    context = {'user': user}
    return render(request, 'user/user.html', context)