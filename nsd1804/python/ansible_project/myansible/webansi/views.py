import shutil
from collections import namedtuple
from ansible.parsing.dataloader import DataLoader
from ansible.vars.manager import VariableManager
from ansible.inventory.manager import InventoryManager
from ansible.playbook.play import Play
from ansible.executor.task_queue_manager import TaskQueueManager
import ansible.constants as C
from django.shortcuts import render, redirect
from .models import HostGroup, AnsibleModule, ModuleArg, Host

def exec_task(servers, mod, args):
    Options = namedtuple('Options',
                         ['connection', 'module_path', 'forks', 'become', 'become_method', 'become_user', 'check',
                          'diff'])
    options = Options(connection='smart', module_path=['/to/mymodules'], forks=10, become=None, become_method=None,
                      become_user=None, check=False, diff=False)

    loader = DataLoader()
    passwords = dict()

    inventory = InventoryManager(loader=loader, sources=['ansicfg/dhosts.py'])

    variable_manager = VariableManager(loader=loader, inventory=inventory)

    play_source = dict(
        name="Ansible Play",
        hosts=servers,
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
    if request.method == 'POST':
        server = request.POST.get('ip')
        if not server:
            server = request.POST.get('group')
        mod = request.POST.get('mod')
        args = request.POST.get('arg')
        exec_task(server, mod, args)

    hosts = Host.objects.all()
    groups = HostGroup.objects.all()
    mods = AnsibleModule.objects.all()
    return render(request, 'tasks.html', {'hosts': hosts, 'groups': groups, 'mods': mods})

def rmarg(request, arg_id):
    a = ModuleArg.objects.get(id=arg_id)
    a.delete()
    return redirect('addmodules')
