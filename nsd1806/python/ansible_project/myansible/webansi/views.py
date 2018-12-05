from django.shortcuts import render
from .models import HostGroup, Host
from .models import AnsiModule
import shutil
from collections import namedtuple
import ansible.constants as C
from ansible.executor.task_queue_manager import TaskQueueManager
from ansible.inventory.manager import InventoryManager
from ansible.parsing.dataloader import DataLoader
from ansible.playbook.play import Play
from ansible.vars.manager import VariableManager

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

def ad_hoc(target, mod, param, hfile=['ansicfg/dhosts.py']):
    Options = namedtuple('Options', ['connection', 'module_path', 'forks', 'become', 'become_method', 'become_user', 'check', 'diff'])
    options = Options(connection='smart', module_path=['/to/mymodules'], forks=10, become=None, become_method=None, become_user=None, check=False, diff=False)

    loader = DataLoader()
    passwords = dict()
    inventory = InventoryManager(loader=loader, sources=hfile)
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    play_source = dict(
            name="Ansible Play",
            hosts=target,
            gather_facts='no',
            tasks=[
                dict(action=dict(module=mod, args=param), register='shell_out'),
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
        # print(request.POST)
        ip = request.POST.get('server')
        group = request.POST.get('hostgroup')
        mod = request.POST.get('module')
        param = request.POST.get('param')
        if ip:
            host = ip
        else:
            host = group
        ad_hoc(host, mod, param)


    groups = HostGroup.objects.all()
    hosts = Host.objects.all()
    mods = AnsiModule.objects.all()
    context = {'groups': groups, 'mods': mods, 'hosts': hosts}
    return render(request, 'tasks.html', context)
