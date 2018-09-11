from django.shortcuts import render, HttpResponse

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
