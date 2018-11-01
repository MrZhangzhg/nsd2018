import shutil
from collections import namedtuple
# ansible.constants是ansible的常量
import ansible.constants as C
# TaskQueueManager用于管理、协调任务的调用、执行
from ansible.executor.task_queue_manager import TaskQueueManager
# InventoryManager用于管理ansible的主机清单
from ansible.inventory.manager import InventoryManager
# DataLoader识别并处理配置文件(ini/yaml/json)
from ansible.parsing.dataloader import DataLoader
# Play用于管理play
from ansible.playbook.play import Play
# VariableManager用于管理ansible的变量
from ansible.vars.manager import VariableManager

# options就是调用ansible命令时的选项
# connection表示连接类型，有local、ssh、smart
# module_path是ansible查找模块的路径
# forks表示生成多少子进程
# become是变成其他用户
# become_method切换用户的方式
# become_user 切换成哪个用户
Options = namedtuple('Options', ['connection', 'module_path', 'forks', 'become', 'become_method', 'become_user', 'check', 'diff'])
options = Options(connection='smart', module_path=['/to/mymodules'], forks=10, become=None, become_method=None, become_user=None, check=False, diff=False)

loader = DataLoader()
passwords = dict()  # 记录各种密码

# 主机清单，sources列出有哪些主机，可以把主机用逗号分开，也可以使用主机文件路径
# inventory = InventoryManager(loader=loader, sources='localhost,')
inventory = InventoryManager(loader=loader, sources=['kvm_ansi/hosts'])

# ansible变量管理
variable_manager = VariableManager(loader=loader, inventory=inventory)

# 定义执行的play
play_source =  dict(
        name = "Ansible Play",
        hosts = 'webservers',  # 在哪些主机上执行命令
        gather_facts = 'no',
        tasks = [  # 执行的命令
            dict(action=dict(module='yum', args='name=vsftpd state=latest'), register='shell_out'),
            # dict(action=dict(module='shell', args='ls'), register='shell_out'),
            # dict(action=dict(module='debug', args=dict(msg='{{shell_out.stdout}}')))
         ]
    )

# 创建Play实例，它会自动通过play_source创建任务对象
play = Play().load(play_source, variable_manager=variable_manager, loader=loader)

# 执行任务
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
    # 清理任务队列对象
    if tqm is not None:
        tqm.cleanup()

    # 删除临时目录
    shutil.rmtree(C.DEFAULT_LOCAL_TMP, True)
