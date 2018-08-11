# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django import forms
from .models import Hosts, Modules
import shutil
from collections import namedtuple
from ansible.parsing.dataloader import DataLoader
from ansible.vars.manager import VariableManager
from ansible.inventory.manager import InventoryManager
from ansible.playbook.play import Play
from ansible.executor.task_queue_manager import TaskQueueManager
import ansible.constants as C


class HostsForm(forms.Form):
    host = forms.CharField(max_length=20, label='主机')
    group = forms.CharField(max_length=20, label='主机组')

class ModuleForm(forms.Form):
    module = forms.CharField(max_length=20, label='模块')
    args = forms.CharField(max_length=100, label='参数')

def add_hosts(request):
    hosts = Hosts.objects.all()
    if request.method == 'POST':
        obj = HostsForm(request.POST)
        if obj.is_valid():
            h = Hosts()
            h.host = obj.cleaned_data['host']
            h.group = obj.cleaned_data['group']
            h.save()
            return redirect(add_hosts)
    else:
        obj = HostsForm()
        return render(request, 'web_ansi/add_hosts.html', {'hosts': hosts, 'obj': obj})

def tasks(request):
    hosts = Hosts.objects.values('host')
    group = Hosts.objects.values('group').distinct()
    modules = Modules.objects.all()
    module_dict = {}
    for m in modules:
        module_dict[m.module_name] = [a.args for a in m.args_set.all()]
    return render(request, 'web_ansi/tasks.py.html', {'hosts': hosts, 'group': group, 'module_dict': module_dict})


def add_modules(request):
    if request.method == 'POST':
        obj = ModuleForm(request.POST)
        if obj.is_valid():
            qset = Modules.objects.filter(module_name__exact=obj.cleaned_data['module'])
            if not qset:
                m = Modules()
                m.module_name = obj.cleaned_data['module']
                m.save()
            else:
                m = qset[0]
            m.args_set.create(args=obj.cleaned_data['args'])
            return redirect(add_modules)
    else:
        modules = Modules.objects.all()
        module_dict = {}
        for m in modules:
            module_dict[m.module_name] = [a.args for a in m.args_set.all()]
        obj = ModuleForm()
        return render(request, 'web_ansi/add_modules.html', {'module_dict': module_dict, 'obj': obj})

def exec_tasks(request):
    module_name = request.POST['module']
    args_name = request.POST['args']
    print(module_name, args_name)
    hostname = request.POST.get('host')
    Options = namedtuple('Options', ['connection', 'module_path', 'forks', 'become', 'become_method', 'become_user', 'check', 'diff'])
    options = Options(connection='ssh', module_path=['/to/mymodules'], forks=10, become=None, become_method=None, become_user=None, check=False, diff=False)
    loader = DataLoader()
    passwords = dict()
    inventory = InventoryManager(loader=loader, sources=['web_ansi/dhosts.py'])
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    play_source =  dict(
            name = "Ansible Play",
            hosts = hostname,
            gather_facts = 'no',
            tasks = [
                dict(action=dict(module=module_name, args=args_name)),
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
    return redirect(tasks)
