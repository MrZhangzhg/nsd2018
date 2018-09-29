import time
from multiprocessing import Process

def f(name):
    print('hello', name)
    print('我是子进程')

if __name__ == '__main__':
    p = Process(target=f, args=('bob',))
    p.start()
    time.sleep(15)
    print('执行主进程的内容了')
