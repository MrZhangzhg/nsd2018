from django.shortcuts import render, redirect, get_object_or_404
from .models import Userdb
from string import ascii_letters, digits
from random import choice
import hmac

def home(request):
    return render(request, 'home.html')

def login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    # user = Userdb.objects.get(username=username)
    user = get_object_or_404(Userdb, username=username)
    # if not user:
    #     return redirect('home')

    h = hmac.new(user.salt.encode(), password.encode(), digestmod='MD5')
    if user.password != h.hexdigest():
        return redirect('home')

    request.session['LOGINED'] = True
    return redirect('protected')


def protected(request):
    is_login = request.session.get('LOGINED', False)
    if not is_login:
        return redirect('home')
    return render(request, 'protected.html')

def randpass(number=8):
    all_chs = ascii_letters + digits
    salt_list = [choice(all_chs) for i in range(number)]
    return ''.join(salt_list)

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        salt = randpass()
        h = hmac.new(salt.encode(), password.encode(), digestmod='MD5')
        Userdb.objects.create(
            username=username,
            salt=salt,
            password=h.hexdigest()
        )

    return render(request, 'register.html')

def vartest(request):
    atuple = ('张三', '李四')
    alist = ['bob', 'alice']
    user_dict = {'name': '王五', 'age': 23, 'phone': '15099776644'}
    is_login = request.session.get('LOGINED', False)
    cities = ['北京', '广州', '杭州', '西安', '长沙', '深圳']
    context = {
        'astr': 'hello world!',
        'num': 100,
        'atuple': atuple,
        'alist': alist,
        'user_dict': user_dict,
        'is_login': is_login,
        'cities': cities
    }
    return render(request, 'vartest.html', context)

