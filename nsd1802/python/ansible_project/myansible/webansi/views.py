# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse
from .models import Host, Group, Module, Args


def mainpage(request):
    return render(request, 'webansi/mainpage.html')

def index(request):
    return render(request, 'webansi/hostinfo.html')

def addhosts(request):
    if request.method == 'POST':
        g = request.POST.get('group')
        ip = request.POST.get('ipaddr')
        h = request.POST.get('hostname')
        gobj = Group.objects.get_or_create(group=g)[0]
        # host = Host(hostname=h, ipaddr=ip, group=gobj)
        # host.save()
        Host.objects.get_or_create(hostname=h, ipaddr=ip, group=gobj)

    host_info = {}
    # {'webservers': ['node1', 'node2'], 'dbservers': 'hosts'}
    groups = Group.objects.all()  # qset
    for g in groups:
        hosts = []
        for host in g.host_set.all():
            hosts.append(host.hostname)
        host_info[g] = hosts

    return render(request, 'webansi/addhosts.html', {'host_info': host_info})

def addmodules(request):
    if request.method == 'POST':
        m = request.POST.get('module')
        a = request.POST.get('args')
        mobj = Module.objects.get_or_create(mod_name=m)[0]
        # args = Args(mod_args=a, mod=mobj)
        # args.save()
        Args.objects.get_or_create(mod_args=a, mod=mobj)

    mod_info = {}
    mods = Module.objects.all()
    for m in mods:
        argss = []
        for args in m.args_set.all():
            argss.append(args.mod_args)
        mod_info[m] = argss

    return render(request, 'webansi/addmodules.html', {'mod_info': mod_info})

def tasks(request):
    return HttpResponse('tasks')
