from django.urls import path
from . import views

app_name = 'user'
urlpatterns = [
    path('<int:user_id>/', views.userHome, name='userHome')
]