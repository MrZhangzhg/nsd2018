import shutil
from collections import namedtuple
from ansible.parsing.dataloader import DataLoader
from ansible.vars.manager import VariableManager
from ansible.inventory.manager import InventoryManager
from ansible.playbook.play import Play
from ansible.executor.task_queue_manager import TaskQueueManager
import ansible.constants as C

# since API is constructed for CLI it expects certain options to always be set, named tuple 'fakes' the args parsing options object
# 设置ansible选项，参见ansible --help
# connection -> local表示本地执行，还有ssh、smart
# module_path指定搜索模块的路径
# forks指的是一次创建多少个子进程
# check只是预计执行的结果，但是不真正的运行命令
# diff用于显示改变了什么
Options = namedtuple('Options', ['connection', 'module_path', 'forks', 'become', 'become_method', 'become_user', 'check', 'diff'])
options = Options(connection='smart', module_path=['/to/mymodules'], forks=10, become=None, become_method=None, become_user=None, check=False, diff=False)

# initialize needed objects
# loader用于查找和分析yaml, json和ini文件
loader = DataLoader() # Takes care of finding and reading yaml, json and ini files
# passwords用于设置各种各样的密码
passwords = dict()

# create inventory, use path to host config file as source or hosts in a comma separated string
# 指定主机清单，有两种方式，一种是用逗号隔开各台主机，另一种是文件列表
# inventory = InventoryManager(loader=loader, sources='localhost,')
inventory = InventoryManager(loader=loader, sources=['myansible/hosts'])

# variable manager takes care of merging all the different sources to give you a unifed view of variables available in each context
# VariableManager用于管理变量
variable_manager = VariableManager(loader=loader, inventory=inventory)

# create datastructure that represents our play, including tasks, this is basically what our YAML loader does internally.
play_source = dict(
        name="My Ansible Play",
        hosts='webservers',  # 在哪些主机上执行命令
        gather_facts='no',   # 不收集主机信息
        tasks=[
            dict(action=dict(module='yum', args='name=vsftpd state=latest'), register='shell_out'),
            # dict(action=dict(module='shell', args='ls'), register='shell_out'),
            # dict(action=dict(module='debug', args=dict(msg='{{shell_out.stdout}}')))
        ]
    )

# Create play object, playbook objects use .load instead of init or new methods,
# this will also automatically create the task objects from the info provided in play_source
# 创建play对象，将前面的对象组合到play中
play = Play().load(play_source, variable_manager=variable_manager, loader=loader)

# Run it - instantiate task queue manager, which takes care of forking and setting up all objects to iterate over host list and tasks
# 运行，创建任务队列管理器，用于管理将要执行的任务
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
        tqm.cleanup()   # 清理任务

    # Remove ansible tmpdir
    # 删除临时目录
    shutil.rmtree(C.DEFAULT_LOCAL_TMP, True)
