from django.urls import path
from django.views.generic import ListView, DetailView
from .models import NewsArticle

app_name = 'news'
urlpatterns = [
    path('', ListView.as_view(model=NewsArticle, template_name='news/list.html',
         queryset=NewsArticle.objects.filter(is_published=True, audience='public'),
         context_object_name='articles'), name='list'),
    path('<slug:slug>/', DetailView.as_view(model=NewsArticle, template_name='news/detail.html'), name='detail'),
]
