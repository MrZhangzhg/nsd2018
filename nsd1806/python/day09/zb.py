import os
import time

pid = os.fork()
if pid:
    print('parent...')
    time.sleep(60)
else:
    print('child...')
    time.sleep(15)

# watch -n1 ps a    # 观察进程的状态
