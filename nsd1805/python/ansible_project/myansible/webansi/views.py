from django.shortcuts import render
from .models import HostGroup

def index(request):
    return render(request, 'index.html')

def mainpage(request):
    return render(request, 'mainpage.html')

def add_hosts(request):
    hostgroup = HostGroup.objects.all()
    return render(request, 'addhosts.html', {'hostgroup': hostgroup})
