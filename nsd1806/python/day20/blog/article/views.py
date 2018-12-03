from django.shortcuts import render, HttpResponse
from .models import Article

def index(request):
    articles = Article.objects.order_by('-pub_date')
    return render(request, 'index.html', {'articles': articles})

def hello(request):
    return HttpResponse('<h1>Hello World!</h1>')
