import os
import time

start = time.time()
print('Start...')
pid = os.fork()
if pid:
    print('in parent...')
    print(os.waitpid(-1, 1))   # 不挂起父进程
    time.sleep(30)
else:
    print('in child')
    time.sleep(10)
end = time.time()
print(end - start)
