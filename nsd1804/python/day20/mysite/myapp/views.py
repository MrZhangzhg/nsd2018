from django.shortcuts import render, HttpResponse, redirect
from .models import Message

def home(request):
    return render(request, 'home.html')

def login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    if username == 'bob' and password == '123456':
        request.session['IS_LOGIN'] = True
        return redirect('protected')
    return redirect('home')

def protected(request):
    is_login = request.session.get('IS_LOGIN', False)
    if is_login:
        return render(request, 'protect.html')
    return redirect('home')

def hello(request):
    return HttpResponse('<h1>Hello World!</h1>')

def message(request):
    if request.method == 'POST':
        msg = request.POST.get('liuyan')
        Message.objects.get_or_create(msg=msg)
        # m = Message(msg=msg)
        # m.save()

    msgs = Message.objects.all()

    return render(request, 'message.html', {'msgs': msgs})
