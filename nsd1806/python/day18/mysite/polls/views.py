from django.shortcuts import render, HttpResponse

def index(request):
    return HttpResponse('<h1>Polls首页</h1>')
