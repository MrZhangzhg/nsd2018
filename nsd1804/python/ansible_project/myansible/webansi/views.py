from django.shortcuts import render, HttpResponse, redirect
from .models import HostGroup, AnsibleModule, ModuleArg

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
        if mod:
            m = AnsibleModule.objects.get_or_create(mod_name=mod)[0]
        if arg:
            m.modulearg_set.get_or_create(arg_text=arg)
    mods = AnsibleModule.objects.all()
    return render(request, 'addmodules.html', {'mods': mods})

def tasks(request):
    return HttpResponse('<h1>tasks</h1>')

def rmarg(request, arg_id):
    a = ModuleArg.objects.get(id=arg_id)
    a.delete()
    return redirect('addmodules')
