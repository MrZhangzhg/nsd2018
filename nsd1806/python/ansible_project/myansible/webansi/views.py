from django.shortcuts import render
from .models import HostGroup, Host
from .models import AnsiModule

def home(request):
    return render(request, 'home.html')

def addhosts(request):
    if request.method == 'POST':
        groupname = request.POST.get('group')
        host = request.POST.get('host')
        ip = request.POST.get('ip')
        if groupname.strip():
            # 取出主机组模型或创建主机组，返回值是(组实例，True/False)
            group = HostGroup.objects.get_or_create(groupname=groupname)[0]
            if host.strip() and ip.strip():
                group.host_set.get_or_create(hostname=host, ipaddr=ip)

    groups = HostGroup.objects.all()
    return render(request, 'addhosts.html', {'groups': groups})

def addmodules(request):
    if request.method == 'POST':
        mod = request.POST.get('module')
        arg = request.POST.get('arg')
        if mod.strip():
            ansi_mod = AnsiModule.objects.get_or_create(module_name=mod)[0]
            if arg.strip():
                ansi_mod.modulearg_set.get_or_create(arg_text=arg)

    mods = AnsiModule.objects.all()
    return render(request, 'addmodules.html', {'mods': mods})

def tasks(request):
    groups = HostGroup.objects.all()
    hosts = Host.objects.all()
    mods = AnsiModule.objects.all()
    context = {'groups': groups, 'mods': mods, 'hosts': hosts}
    return render(request, 'tasks.html', context)
