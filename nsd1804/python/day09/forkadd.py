import time
import os

def add():
    result = 0
    for i in range(1, 50000001):
        result += i
    print(result)

if __name__ == '__main__':
    start = time.time()
    for i in range(2):
        pid = os.fork()
        if not pid:
            add()
            exit(0)
    for i in range(2):
        os.waitpid(-1, 0)  # 因为有两个子进程，所以要waitpid两次
    end = time.time()
    print(end - start)
