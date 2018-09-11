from django.shortcuts import render, HttpResponse

def hello(request, age):
    return HttpResponse('Hello World! %s' % age)
