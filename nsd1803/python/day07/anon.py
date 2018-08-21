from random import randint

def func1(x):
    return x % 2

def func2(x):
    return x * 2 + 1

if __name__ == '__main__':
    nums = [randint(1, 100) for i in range(10)]
    print(nums)
    # filter的第一个参数是函数，这种函数叫作高阶函数
    # 将nums列表中的每一项交给func1处理，返回True保留，返回False过滤掉
    print(list(filter(func1, nums)))
    print(list(filter(lambda x: x % 2, nums)))

    print(list(map(func2, nums)))  # 将nums列表中的每个数字交给func2加工一下
    print(list(map(lambda x: x * 2 + 1, nums)))



