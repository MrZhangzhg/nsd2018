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
        tlist.append(t)  # 将线程加入到列表
        t.start()
    for td in tlist:
        td.join()  # 与waitpid类似，等待工作线程结束之后才会继续向下执行
    end = time.time()
    print(end - start)
