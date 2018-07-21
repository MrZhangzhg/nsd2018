from random import randint

def func1(x):
    return x % 2

if __name__ == '__main__':
    alist = [randint(1, 100) for i in range(10)]
    print(alist)
    # filter要求第一个参数是函数，该函数必须返回True或False
    # 执行时把alist的每一项作为 func1的参数，返回真留下，否则过滤掉
    result = filter(func1, alist)  # 高阶函数
    print(list(result))
    result2 = filter(lambda x: x % 2, alist)
    print(list(result2))
