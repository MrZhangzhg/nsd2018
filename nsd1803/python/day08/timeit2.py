import time

def timeit(func):
    start = time.time()
    func()
    end = time.time()
    print(end - start)

def funca():
    time.sleep(5)

def funcb():
    print('Hellow World!')

if __name__ == '__main__':
    timeit(funca)
    timeit(funcb)
