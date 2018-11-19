import os

print('Hello World!')
pid = os.fork()   # 父进程的pid变量是非0值，子进程的pid变量值为0
if pid:
    print('父进程... ...')   # 父进程打印
else:
    print('子进程... ...')   # 子进程打印

print('您好!')   # 父子进程都打印
