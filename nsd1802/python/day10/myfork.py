import os

print('starting...')
os.fork()  # 生成子进程，后续代码同时在父子进程中执行
print('Hello World!')
