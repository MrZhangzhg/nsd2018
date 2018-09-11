from django.shortcuts import render, HttpResponse, redirect

def hello(request, age):
    return HttpResponse('Hello World! %s' % age)

def info(request, name, age):
    return HttpResponse('%s is %s years old.' % (name, age))

def index(request):
    if request.method == 'POST':
        user = request.POST.get('xm')
    else:
        user = None
    return render(request, 'index.html', {'user': user})

def home(request):
    return render(request, 'home.html')

def login(request):
    user = request.POST.get('username')
    passwd = request.POST.get('password')
    if user == 'tom' and passwd == '123456':
        request.session['IS_LOGINED'] = True
        return redirect('protect')
    else:
        return redirect('home')

def protect(request):
    is_login = request.session.get('IS_LOGINED', False)
    if is_login:
        return render(request, 'protect.html')
    return redirect('home')





