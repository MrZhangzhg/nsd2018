from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def mainpage(request):
    return render(request, 'mainpage.html')
