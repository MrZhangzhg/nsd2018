# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse
from .models import Group, Module, Host

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
        hostgroup.host_set.get_or_create(hostname=host, ipaddr=ip)

    groups = Group.objects.all()
    return render(request, 'webansi/addhosts.html', {'groups': groups})

def addmodules(request):
    if request.method == 'POST':
        mod = request.POST.get('mod')
        param = request.POST.get('param')
        module = Module.objects.get_or_create(module_name=mod)[0]
        module.args_set.get_or_create(args_text=param)

    modules = Module.objects.all()
    return render(request, 'webansi/addmodules.html', {'modules': modules})

def tasks(request):
    groups = Group.objects.all()
    hosts = Host.objects.all()
    modules = Module.objects.all()
    context = {'groups': groups, 'hosts': hosts, 'modules': modules}
    return render(request, 'webansi/tasks.html', context)
