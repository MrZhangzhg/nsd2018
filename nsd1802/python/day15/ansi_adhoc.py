#!/usr/bin/env python
# coding: utf8

import shutil
from collections import namedtuple
from ansible.parsing.dataloader import DataLoader
from ansible.vars.manager import VariableManager
from ansible.inventory.manager import InventoryManager
from ansible.playbook.play import Play
from ansible.executor.task_queue_manager import TaskQueueManager
import ansible.constants as C

# 因为不想使用自定义输出，所以删除了CallBack
# since API is constructed for CLI it expects certain options to always be set, named tuple 'fakes' the args parsing options object
Options = namedtuple('Options', ['connection', 'module_path', 'forks', 'become', 'become_method', 'become_user', 'check', 'diff'])
# 连接可以设置为local/ssh/smart
# local表示本地执行，ssh表示使用ssh连接，smart表示智能判断
options = Options(connection='smart', module_path=['/to/mymodules'], forks=10, become=None, become_method=None, become_user=None, check=False, diff=False)

# initialize needed objects
loader = DataLoader() # 用于分析json/yaml文件
passwords = dict()

# create inventory, use path to host config file as source or hosts in a comma separated string
# 主机清单，使用字符串主机名，逗号分隔
# 也可以使用列表，列表中列出主机清单文件路径
# inventory = InventoryManager(loader=loader, sources='localhost,node2.tedu.cn')
inventory = InventoryManager(loader=loader, sources=['myansi/hosts'])

# variable manager takes care of merging all the different sources to give you a unifed view of variables available in each context
# 变量管理器
variable_manager = VariableManager(loader=loader, inventory=inventory)

# create datastructure that represents our play, including tasks, this is basically what our YAML loader does internally.
play_source = dict(
        name="Ansible Play",
        hosts='webservers',  # 在上面inventory定义的myansi/hosts中查找
        gather_facts='no',
        tasks=[
            # dict(action=dict(module='shell', args='ls'), register='shell_out'),
            # dict(action=dict(module='shell', args='useradd tom'), register='shell_out'),
            # dict(action=dict(module='shell', args='id tom'), register='shell_out'),
            dict(action=dict(module='yum', args='name=vsftpd state=latest'), register='shell_out'),
            # dict(action=dict(module='debug', args=dict(msg='{{shell_out.stdout}}')))
         ]
    )

# Create play object, playbook objects use .load instead of init or new methods,
# this will also automatically create the task objects from the info provided in play_source
play = Play().load(play_source, variable_manager=variable_manager, loader=loader)

# Run it - instantiate task queue manager, which takes care of forking and setting up all objects to iterate over host list and tasks
tqm = None
try:
    tqm = TaskQueueManager(
              inventory=inventory,
              variable_manager=variable_manager,
              loader=loader,
              options=options,
              passwords=passwords,
          )
    result = tqm.run(play) # most interesting data for a play is actually sent to the callback's methods
finally:
    # we always need to cleanup child procs and the structres we use to communicate with them
    if tqm is not None:
        tqm.cleanup()

    # Remove ansible tmpdir
    shutil.rmtree(C.DEFAULT_LOCAL_TMP, True)
