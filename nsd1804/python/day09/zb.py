import time
import os

# print('starting...')
# pid = os.fork()
# if pid:
#     print('in parent.')
#     time.sleep(60)
# else:
#     print('in child')
#     time.sleep(15)
# watch -n1 ps a
############################################
print('starting...')
pid = os.fork()
if pid:
    print('in parent.')
    print(os.waitpid(-1, 0))  # -1是固定的，0表示挂起父进程，直到子进程被处理
    # waitpid处理了僵尸进程，返回值是(僵尸进程pid, 0)
    print('go on...')  # 子进程变成僵尸进程，被处理后执行
else:
    print('in child')
    time.sleep(15)
############################################
# print('starting...')
# pid = os.fork()
# if pid:
#     print('in parent.')
#     print(os.waitpid(-1, 1))  # -1是固定的，1表示不挂起父进程
#     # 子进程还没有变成僵尸进程，返回值是(0, 0)
#     print('go on...')  # 立即执行
# else:
#     print('in child')
#     time.sleep(15)
#     print('child go on...')
