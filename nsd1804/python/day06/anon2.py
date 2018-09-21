from random import randint

def mydiv(x):
    return x % 2

def func1(x):
    return x * 2 + 1

if __name__ == '__main__':
    alist = [randint(1, 100) for i in range(10)]
    print(alist)
    print(list(filter(mydiv, alist)))  # alist中的每一项都作为mydiv的参数，如果返回值是True就留下来，否则过滤掉
    print(list(filter(lambda x: x % 2, alist)))
    print(list(map(func1, alist)))  # alist中的每每一项都作为func1的参数，处理后把结果返回
    print(list(map(lambda x: x * 2 + 1, alist)))
