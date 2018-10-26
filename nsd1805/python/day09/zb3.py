import os
import time

pid = os.fork()

if pid:
    print('in parent')
    time.sleep(10)
    print(os.waitpid(-1, 0))  # 0表示挂起父进程
    # 僵尸进程被处理掉，返回值是(子进程pid, 0)
    time.sleep(50)
else:
    print('in child')
    time.sleep(15)
