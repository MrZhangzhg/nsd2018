import time
import threading

def add():
    result = 0
    for i in range(1, 50000001):
        result += i
    print(result)

if __name__ == '__main__':
    start = time.time()
    tlist = []
    for i in range(2):
        t = threading.Thread(target=add)
        tlist.append(t)
        t.start()
    for t in tlist:
        t.join()  # 挂起主线程，等到工作线程结束后才会继续主线程
    end = time.time()
    print(end - start)
