# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import shutil
from collections import namedtuple
from ansible.parsing.dataloader import DataLoader
from ansible.vars.manager import VariableManager
from ansible.inventory.manager import InventoryManager
from ansible.playbook.play import Play
from ansible.executor.task_queue_manager import TaskQueueManager
import ansible.constants as C
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

def exec_task(dest, mod, args):
    Options = namedtuple('Options',
         ['connection', 'module_path', 'forks', 'become', 'become_method', 'become_user', 'check', 'diff'])
    options = Options(connection='smart', module_path=['/to/mymodules'], forks=10, become=None, become_method=None,
                      become_user=None, check=False, diff=False)

    loader = DataLoader()
    passwords = dict()

    inventory = InventoryManager(loader=loader, sources=['ansicfg/dhosts.py'])
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    play_source = dict(
        name="Ansible Play",
        hosts=dest,
        gather_facts='no',
        tasks=[
            dict(action=dict(module=mod, args=args), register='shell_out'),
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

def tasks(request):
    if request.method == 'POST':
        ip = request.POST.get('ipaddr')
        group = request.POST.get('group')
        mod = request.POST.get('module')
        args = request.POST.get('args')
        print ip, group, mod, args
        if ip:
            dest = ip
        else:
            dest = group
        exec_task(dest, mod, args)

    hosts = list(Host.objects.all())
    groups = list(Group.objects.all())
    mod_info = {}
    mods = Module.objects.all()
    for m in mods:
        argss = []
        for args in m.args_set.all():
            argss.append(args.mod_args)
        mod_info[m] = argss
    result = {'hosts': hosts, 'groups': groups, 'mods': mods, 'args': args, 'mod_info': mod_info}

    return render(request, 'webansi/tasks.html', result)
