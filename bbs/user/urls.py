import imp
from django.urls import path, include
from . import views
app_name = 'user'
urlpatterns = [
    # path('', include('django.contrib.auth.urls'))
    path('',views.loginHTML)
]