from functools import partial

def add(a, b, c, d):
    return a + b + c + d

if __name__ == '__main__':
    print(add(10, 20, 30, 5))
    print(add(10, 20, 30, 15))
    print(add(10, 20, 30, 25))
    print(add(10, 20, 30, 35))
    myadd = partial(add, 10, 20, 30)
    print(myadd(5))
    print(myadd(15))
    print(myadd(25))
    print(myadd(35))


