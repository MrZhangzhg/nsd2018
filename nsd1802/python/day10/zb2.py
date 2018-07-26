import os
import time

pid = os.fork()

if pid:
    print('In parent. sleeping...')
    print(os.waitpid(-1, 1))  # 无僵尸进程可以处理，返回0
    time.sleep(20)
    print(os.waitpid(-1, 1))  # 处理僵尸进程，返回子进程PIP
    time.sleep(60)
    print('parent done.')
else:
    print('in child. sleeping...')
    time.sleep(10)
    print('child done')

# watch -n1 ps a  当子进程成为僵尸进程时，显示为Z
# kill 试图杀死僵尸进程、父进进程，查看结果
