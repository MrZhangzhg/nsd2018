# 4!=4X3X2X1
# 4!=4X3!
# 4!=4X3X2!
# 4!=4X3X2X1!

def func1(x):
    if x == 1:
        return 1   # 虽然有多个return，但只会返回一次
    return x * func1(x - 1)
    #      4 * func1(3)
    #      4 * 3 * func1(2)
    #      4 * 3 * 2 * func1(1)
    #      4 * 3 * 2 * 1

if __name__ == '__main__':
    print(func1(5))
    print(func1(6))
