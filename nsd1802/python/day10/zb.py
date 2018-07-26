import os
import time

pid = os.fork()

if pid:
    print('In parent. sleeping...')
    time.sleep(60)
    print('parent done.')
else:
    print('in child. sleeping...')
    time.sleep(10)
    print('child done')

# watch -n1 ps a  当子进程成为僵尸进程时，显示为Z
# kill 试图杀死僵尸进程、父进进程，查看结果
