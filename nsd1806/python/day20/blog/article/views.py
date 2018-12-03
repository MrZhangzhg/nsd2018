from django.shortcuts import render, HttpResponse, redirect
from .models import Article
from django.utils import timezone

def home(request):
    return render(request, 'home.html')

def login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')

    if username == 'user1' and password == '123456':
        request.session['IS_LOGINED'] = True
        return redirect('protected')

    return redirect('home')

def protected(request):
    is_logined = request.session.get('IS_LOGINED', False)
    if is_logined:
        return render(request, 'protected.html')
    return redirect('home')

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
