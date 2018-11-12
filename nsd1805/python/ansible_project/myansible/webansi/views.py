from django.shortcuts import render
from .models import HostGroup, AnsiModule

def index(request):
    return render(request, 'index.html')

def mainpage(request):
    return render(request, 'mainpage.html')

def add_hosts(request):
    if request.method == 'POST':
        group = request.POST.get('group').strip()
        host = request.POST.get('host').strip()
        ipaddr = request.POST.get('ipaddr').strip()
        if group:
            g = HostGroup.objects.get_or_create(hostgroup=group)[0]
            if host and ipaddr:
                g.host_set.get_or_create(hostname=host, ipaddr=ipaddr)
    hostgroup = HostGroup.objects.all()
    return render(request, 'addhosts.html', {'hostgroup': hostgroup})

def add_modules(request):
    if request.method == 'POST':
        mod = request.POST.get('mod').strip()
        args = request.POST.get('args').strip()
        if mod and args:
            m = AnsiModule.objects.get_or_create(mod_name=mod)[0]
            m.modargs_set.get_or_create(args_text=args)
    all_modules = AnsiModule.objects.all()
    return render(request, 'addmodules.html', {'all_modules': all_modules})

