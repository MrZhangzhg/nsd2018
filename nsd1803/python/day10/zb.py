import os
import time

pid = os.fork()
if pid:
    print('in parent, sleeping...')
    time.sleep(10)
    print(os.waitpid(-1, 1))  # 收拾子进程，如果子进程是僵尸进程，释放它
                              # 如果不是，父进程什么也不做，继续向下执行
    time.sleep(20)
else:
    print('in child, sleeping...')
    time.sleep(15)





