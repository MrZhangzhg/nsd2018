from django.shortcuts import render, redirect
from .models import HostGroup, AnsibleModule, ModuleArg, Host

def index(request):
    return render(request, 'index.html')

def mainpage(request):
    return render(request, 'mainpage.html')

def addhosts(request):
    if request.method == 'POST':
        group = request.POST.get('group')
        host = request.POST.get('host')
        ip = request.POST.get('ip')
        g = HostGroup.objects.get_or_create(group_name=group)[0]
        g.host_set.get_or_create(hostname=host, ipaddr=ip)

    groups = HostGroup.objects.all()
    return render(request, 'addhosts.html', {'groups': groups})

def addmodules(request):
    if request.method == 'POST':
        mod = request.POST.get('mod_name')
        arg = request.POST.get('arg')
        if mod and arg:
            m = AnsibleModule.objects.get_or_create(mod_name=mod)[0]
            m.modulearg_set.get_or_create(arg_text=arg)
    mods = AnsibleModule.objects.all()
    return render(request, 'addmodules.html', {'mods': mods})

def tasks(request):
    hosts = Host.objects.all()
    groups = HostGroup.objects.all()
    mods = AnsibleModule.objects.all()
    return render(request, 'tasks.html', {'hosts': hosts, 'groups': groups, 'mods': mods})

def rmarg(request, arg_id):
    a = ModuleArg.objects.get(id=arg_id)
    a.delete()
    return redirect('addmodules')
