from django.shortcuts import render, redirect
from .models import Userdb
import hmac

def home(request):
    return render(request, 'home.html')

def login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = Userdb.objects.get(username=username)
    if not user:
        return redirect('home')

    h = hmac.new(user.salt.encode(), password.encode(), digestmod='MD5')
    if user.password != h.hexdigest():
        return redirect('home')

    request.session['LOGINED'] = True
    return redirect('protected')


def protected(request):

    return render(request, 'protected.html')
