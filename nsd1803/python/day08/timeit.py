import time

def deco(func):
    def timeit():
        start = time.time()
        func()
        end = time.time()
        print(end - start)
    return timeit

@deco
def funca():
    time.sleep(5)

@deco
def funcb():
    print('Hellow World!')

if __name__ == '__main__':
    funca()
    funcb()
