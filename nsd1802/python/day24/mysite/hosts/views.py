from django.shortcuts import render, redirect
from .models import Host

def add(request):
    pass


def addhost(request):
    hostname = request.POST.get('hostname')
    ip = request.POST.get('ipaddr')
    group = request.POST.get('group')
    Host.objects.get_or_create(hostname=hostname, ip_addr=ip, group=group)
    # host = Host(hostname=hostname, ip_addr=ip, group=group)
    # host.save()
    return redirect('add')
