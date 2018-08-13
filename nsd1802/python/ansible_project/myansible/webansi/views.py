# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse

def mainpage(request):
    return render(request, 'webansi/mainpage.html')

def index(request):
    return render(request, 'webansi/hostinfo.html')

def addhosts(request):
    return render(request, 'webansi/addhosts.html')

def addmodules(request):
    return HttpResponse('addmodules')

def tasks(request):
    return HttpResponse('tasks')
