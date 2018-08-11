# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse

def mainpage(request):
    return HttpResponse('mainpage')

def index(request):
    return HttpResponse('index')

def addhosts(request):
    return HttpResponse('addhosts')

def addmodules(request):
    return HttpResponse('addmodules')

def tasks(request):
    return HttpResponse('tasks')
