def func(x):   # 递归函数，自己再调用自己
    if x == 1:
        return 1
    return x * func(x - 1)
         # 5 * func(4)
         # 5 * 4 * func(3)
         # 5 * 4 * 3 * func(2)
         # 5 * 4 * 3 * 2 * func(1)
         # 5 * 4 * 3 * 2 * 1

if __name__ == '__main__':
    print(func(5))
    print(func(6))

# 5!=5X4X3X2X1
# 5!=5X4!
# 5!=5X4X3!
# 5!=5X4X3X2!
# 5!=5X4X3X2X1!
