<<<<<<< HEAD
import imp
from django.urls import path, include
from . import views
app_name = 'user'
urlpatterns = [
    # path('', include('django.contrib.auth.urls'))
    path('',views.loginHTML)
=======
import imp
from django.urls import path, include
from . import views

app_name = 'user'
urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('<str:user_name>/', views.userHome, name='userHome')
>>>>>>> b78de72eb2f9d273799cec6582fef8fac4235eb9
]