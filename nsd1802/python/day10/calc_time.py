import time

def calc():
    result = 0
    for i in range(1, 50000001):
        result += i
    print(result)

if __name__ == '__main__':
    start = time.time()
    calc()
    calc()
    end = time.time()
    print(end - start)
