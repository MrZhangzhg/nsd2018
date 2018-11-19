import os
import time

def add(n):
    result = 0
    for i in range(1, n):
        result += i
    print(result)

if __name__ == '__main__':
    start = time.time()
    for i in range(2):
        pid = os.fork()
        if not pid:
            add(50000001)
            exit()
    for i in range(2):
        os.waitpid(-1, 0)
    end = time.time()
    print(end - start)
