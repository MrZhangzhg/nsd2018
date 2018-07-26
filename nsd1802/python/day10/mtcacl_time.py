import time
import threading

def calc():
    result = 0
    for i in range(1, 50000001):
        result += i
    print(result)

if __name__ == '__main__':
    start = time.time()
    t1 = threading.Thread(target=calc)
    t1.start()
    t2 = threading.Thread(target=calc)
    t2.start()
    t1.join()  # 挂起主进程，当t1线程执行完后才继续向下执行
    t2.join()
    end = time.time()
    print(end - start)
