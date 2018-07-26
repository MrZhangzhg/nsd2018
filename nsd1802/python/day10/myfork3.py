import os

for i in range(5):
    pid = os.fork()  # 父进程的工作是生成子进程
    if not pid:  # 如果是子进程，工作完后，结束，不要进入循环
        print('hello')
        exit()
