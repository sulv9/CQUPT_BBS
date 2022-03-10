from django.urls import path, include
from . import views
app_name = 'user'
urlpatterns = [
    # 处理登录 POST 请求
    path('',views.loginHTML),
    # 处理注销 POST 请求
    path('logOut',views.logOut),
]