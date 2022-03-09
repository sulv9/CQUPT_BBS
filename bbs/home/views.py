from django.shortcuts import render
from user.models import Topic, Article

# Create your views here.
def home(request):
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