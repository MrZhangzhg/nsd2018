# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse
from .models import Group

def mainpage(request):
    return render(request, 'webansi/mainpage.html')

def index(request):
    return render(request, 'webansi/index.html')

def addhosts(request):
    if request.method == 'POST':
        group = request.POST.get('group')
        host = request.POST.get('host')
        ip = request.POST.get('ip')
        hostgroup = Group.objects.get_or_create(hostgroup=group)[0]
        print(hostgroup)
        hostgroup.host_set.get_or_create(hostname=host, ipaddr=ip)

    groups = Group.objects.all()
    return render(request, 'webansi/addhosts.html', {'groups': groups})

def addmodules(request):
    return HttpResponse('add modules')

def tasks(request):
    return HttpResponse('execute task')
