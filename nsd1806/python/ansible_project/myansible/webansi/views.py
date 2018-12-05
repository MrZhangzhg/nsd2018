from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def addhosts(request):
    return render(request, 'addhosts.html')
