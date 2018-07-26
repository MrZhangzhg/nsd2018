import os

print('starting...')

pid = os.fork()  # 返回值是个数字，对于父进程，返回值是子进程PID，子进程是0
if pid:
    print('In parent')
else:
    print('In child')

print('Done')
