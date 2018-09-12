# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse

def mainpage(request):
    return render(request, 'webansi/mainpage.html')

def index(request):
    return HttpResponse('web ansi index')

def addhosts(request):
    return HttpResponse('add hosts')

def addmodules(request):
    return HttpResponse('add modules')

def tasks(request):
    return HttpResponse('execute task')
