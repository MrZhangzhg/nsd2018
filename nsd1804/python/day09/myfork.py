import os

print('starting...')
os.fork()   # 将产生子进程，后续代码会在父子进程里都执行
print('Hello World!')
