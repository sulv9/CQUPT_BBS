<<<<<<< HEAD
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home')
=======
from django.urls import path
from . import views

app_name = 'home'
urlpatterns = [
    path('', views.home, name='home'),
    path('article/<int:article_id>/', views.article, name='article'),
    path('topic/<int:topic_id>', views.topic, name="topic")
>>>>>>> b78de72eb2f9d273799cec6582fef8fac4235eb9
]