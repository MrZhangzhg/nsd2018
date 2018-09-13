# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse
from .models import Group, Module, Host
import shutil
from collections import namedtuple
from ansible.parsing.dataloader import DataLoader
from ansible.vars.manager import VariableManager
from ansible.inventory.manager import InventoryManager
from ansible.playbook.play import Play
from ansible.executor.task_queue_manager import TaskQueueManager
import ansible.constants as C

def exec_task(host_file, host, mod, param):
    Options = namedtuple('Options', ['connection', 'module_path', 'forks', 'become', 'become_method', 'become_user', 'check', 'diff'])
    options = Options(connection='smart', module_path=['/to/mymodules'], forks=10, become=None, become_method=None, become_user=None, check=False, diff=False)
    loader = DataLoader()
    passwords = dict()
    inventory = InventoryManager(loader=loader, sources=host_file)
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    play_source = dict(
            name="Ansible Play",
            hosts=host,
            gather_facts='no',
            tasks=[
                dict(action=dict(module=mod, args=param), register='shell_out'),
                dict(action=dict(module='debug', args=dict(msg='{{shell_out}}')))
             ]
        )
    play = Play().load(play_source, variable_manager=variable_manager, loader=loader)
    tqm = None
    try:
        tqm = TaskQueueManager(
                  inventory=inventory,
                  variable_manager=variable_manager,
                  loader=loader,
                  options=options,
                  passwords=passwords,
              )
        result = tqm.run(play)
    finally:
        if tqm is not None:
            tqm.cleanup()
        shutil.rmtree(C.DEFAULT_LOCAL_TMP, True)

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
    if request.method == 'POST':
        ip = request.POST.get('ip')
        hostgroup = request.POST.get('hostgroup')
        if ip:
            hmod = request.POST.get('hmod')
            hparam = request.POST.get('hparam')
            exec_task(['ansicfg/dhosts.py'], ip, hmod, hparam)
        else:
            gmod = request.POST.get('gmod')
            gparam = request.POST.get('gparam')
            exec_task(['ansicfg/dhosts.py'], hostgroup, gmod, gparam)

    groups = Group.objects.all()
    hosts = Host.objects.all()
    modules = Module.objects.all()
    context = {'groups': groups, 'hosts': hosts, 'modules': modules}
    return render(request, 'webansi/tasks.html', context)
