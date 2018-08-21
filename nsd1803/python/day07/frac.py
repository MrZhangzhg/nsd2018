# 5!=5X4X3X2X1
# 5!=5X4!
# 5!=5X4X3!
# 5!=5X4X3X2!
# 5!=5X4X3X2X1!
# 1! = 1

def func(x):
    if x == 1:
        return x

    return x * func(x - 1)
          #3*func(2)
          #3*2*func(1)
          #3*2*1

if __name__ == '__main__':
    print(func(3))
    print(func(4))
