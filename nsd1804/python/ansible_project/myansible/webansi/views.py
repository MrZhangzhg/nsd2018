from django.shortcuts import render, HttpResponse
from .models import HostGroup

def index(request):
    return render(request, 'index.html')

def mainpage(request):
    return render(request, 'mainpage.html')

def addhosts(request):
    groups = HostGroup.objects.all()
    return render(request, 'addhosts.html', {'groups': groups})

def addmodules(request):
    return HttpResponse('<h1>add modules</h1>')

def tasks(request):
    return HttpResponse('<h1>tasks</h1>')
