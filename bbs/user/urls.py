from django.urls import path
from . import views

app_name = 'user'
urlpatterns = [
    path('<int:user_id>/', views.userHome, name='userHome'),
    # 处理登录 POST 请求
    path('',views.loginHTML),
    # 处理注销 POST 请求
    path('logOut',views.logOut),
]