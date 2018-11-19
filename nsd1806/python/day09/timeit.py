import time

def add(n):
    result = 0
    for i in range(1, n):
        result += i
    print(result)

if __name__ == '__main__':
    start = time.time()
    add(50000001)
    add(50000001)
    end = time.time()
    print(end - start)
