from django.shortcuts import render, HttpResponse

def index(request):
    return render(request, 'index.html')

def mainpage(request):
    return HttpResponse('<h1>main page</h1>')

def addhosts(request):
    return HttpResponse('<h1>add hosts</h1>')

def addmodules(request):
    return HttpResponse('<h1>add modules</h1>')

def tasks(request):
    return HttpResponse('<h1>tasks</h1>')
