import os
import time

pid = os.fork()

if pid:
    print('in parent')
    time.sleep(10)
    print(os.waitpid(-1, 1))
    # 父进程发现子进程不是僵尸进程，返回(0, 0)，父进程不挂起，继续向下执行
    # 僵尸进程没有得到处理
    time.sleep(50)
else:
    print('in child')
    time.sleep(15)
