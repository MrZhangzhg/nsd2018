from django.shortcuts import render
from .models import HostGroup, AnsiModule, Host
from collections import namedtuple
import ansible.constants as C
from ansible.executor.task_queue_manager import TaskQueueManager
from ansible.inventory.manager import InventoryManager
from ansible.parsing.dataloader import DataLoader
from ansible.playbook.play import Play
from ansible.vars.manager import VariableManager
import shutil

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

def exec_task(target, mod, args, inventory_path=['ansicfg/dhosts.py']):
    Options = namedtuple('Options', ['connection', 'module_path', 'forks', 'become', 'become_method', 'become_user', 'check', 'diff'])
    options = Options(connection='smart', module_path=['/to/mymodules'], forks=10, become=None, become_method=None, become_user=None, check=False, diff=False)
    loader = DataLoader()
    passwords = dict()
    inventory = InventoryManager(loader=loader, sources=inventory_path)
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    play_source =  dict(
            name="Ansible Play",
            hosts=target,
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
        target = request.POST.get('host')
        if not target:
            target = request.POST.get('group')
        mod = request.POST.get('mod')
        args = request.POST.get('arg')
        exec_task(target, mod, args)

    hosts = Host.objects.all()
    hostgroup = HostGroup.objects.all()
    all_modules = AnsiModule.objects.all()
    context = {'hosts': hosts, 'hostgroup': hostgroup, 'all_modules': all_modules}
    return render(request, 'tasks.html', context)
