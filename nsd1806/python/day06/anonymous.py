from random import randint

def func1(x):
    return x % 2

def func2(x):
    return x * 2 + 1

if __name__ == '__main__':
    nums = [randint(1, 100) for i in range(10)]
    print(nums)  # [14, 54, 61, 23, 31, 6, 72, 57, 21, 8]
    print(list(filter(func1, nums)))
    print(list(filter(lambda x: x % 2, nums)))
    print(list(map(func2, nums)))
    print(list(map(lambda x: x * 2 + 1, nums)))
