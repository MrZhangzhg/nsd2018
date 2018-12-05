from django.shortcuts import render
from .models import HostGroup

def home(request):
    return render(request, 'home.html')

def addhosts(request):
    groups = HostGroup.objects.all()
    return render(request, 'addhosts.html', {'groups': groups})
