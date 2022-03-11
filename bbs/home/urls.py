from django.urls import path
from . import views

app_name = 'home'
urlpatterns = [
    path('', views.home, name='home'),
    path('article/<int:article_id>/', views.article, name='article'),
    path('topic/<int:topic_id>', views.topic, name="topic"),
    path('loginError',views.loginError),
    path('signOutError',views.signOutError),
]