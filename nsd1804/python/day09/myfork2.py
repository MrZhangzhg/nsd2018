import os

for i in range(3):
    pid = os.fork()
    if not pid:  # 如果是子进程，打印hello
        print('hello')
        exit(0)  # 子进程工作完要结束，否则它在循环结构中，还能再产生孙进程
