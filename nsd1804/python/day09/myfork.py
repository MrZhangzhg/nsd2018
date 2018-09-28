import os

# print('starting...')
# os.fork()   # 将产生子进程，后续代码会在父子进程里都执行
# print('Hello World!')
#################################################
print('starting...')
pid = os.fork()  # fork对父进程返回子进程PID，对子进程返回0
if pid:
    print('Hello from parent')
else:
    print('Hello from child')

print('Hello from both')
