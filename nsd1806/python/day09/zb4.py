import os
import time


pid = os.fork()
if not pid:
    print('in child1...')
    time.sleep(15)
    print('child1 done')
    exit()

pid = os.fork()
if not pid:
    print('in child2...')
    time.sleep(20)
    print('child2 done')
    exit()

time.sleep(25)  # 父进程睡眠时间比两个子进程都长，保证waitpid调用时，子进程已经变成僵尸进程
print(os.waitpid(-1, 1))  # 一个waitpid只能处理一个僵尸进程
time.sleep(10)
