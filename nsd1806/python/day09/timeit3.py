import threading
import time

def add(n):
    result = 0
    for i in range(1, n):
        result += i
    print(result)

if __name__ == '__main__':
    start = time.time()
    tlist = []
    for i in range(2):
        t = threading.Thread(target=add, args=(50000001,))
        tlist.append(t)   # 将线程加入列表
        t.start()
    for th in tlist:
        th.join()   # 在列表中取中线程，主线程等待它结束后再向下执行
    end = time.time()
    print(end - start)
