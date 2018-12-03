from django.shortcuts import render, HttpResponse
from .models import Article
from django.utils import timezone

def index(request):
    if request.method == 'POST':
        # print(request.POST)
        title = request.POST.get('title')
        content = request.POST.get('content')
        if title.strip() and content.strip():
            # Article.objects.create(
            #     title=title,
            #     pub_date= timezone.now(),
            #     text=content
            # )
            Article.objects.get_or_create(
                title=title,
                pub_date=timezone.now(),
                text=content
            )

    articles = Article.objects.order_by('-pub_date')
    return render(request, 'index.html', {'articles': articles})

def hello(request):
    return HttpResponse('<h1>Hello World!</h1>')
