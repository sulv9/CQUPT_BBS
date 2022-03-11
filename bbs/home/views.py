#  Models and Redircet

from django.shortcuts import render,redirect
from user.models import Topic, Article

# Http
from django.http import HttpRequest,HttpResponse


# Home Views
def home(request:HttpRequest):
    topics = Topic.objects.order_by('pub_time')[:7]
    articles = Article.objects.order_by('pub_time')
    context = {'topics': topics, 'articles': articles}
    return render(request, 'home/home.html', context)


def article(request, article_id):
    article = Article.objects.get(id=article_id)
    context = {'article': article}
    return render(request, 'home/article.html', context)

def topic(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    articles = topic.article_set.order_by('-pub_time')
    context = {'topic': topic, 'articles': articles}
    return render(request, 'home/topic.html', context)


def loginError(request):
    topics = Topic.objects.order_by('pub_time')[:7]
    articles = Article.objects.order_by('pub_time')
    context = {'topics': topics, 'articles': articles}
    return render(request,'home/loginError.html',context)

def signOutError(request):
    topics = Topic.objects.order_by('pub_time')[:7]
    articles = Article.objects.order_by('pub_time')
    context = {'topics': topics, 'articles': articles}
    return render(request,'home/out.html',context)

def signUpError(request):
    topics = Topic.objects.order_by('pub_time')[:7]
    articles = Article.objects.order_by('pub_time')
    context = {'topics': topics, 'articles': articles}
    return render(request,'home/signup.html',context)