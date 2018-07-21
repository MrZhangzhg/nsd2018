from functools import partial

def foo(a, b, c, d, f):
    return a + b + c + d + f

if __name__ == '__main__':
    print(foo(10, 20, 30, 40, 5))
    print(foo(10, 20, 30, 40, 25))
    print(foo(10, 20, 30, 40, 69))
    print(foo(10, 20, 30, 40, 32))
    add = partial(foo, a=10, b=20, c=30, d=40)
    print(add(f=5))  # foo(10, 20, 30, 40, 5)
    print(add(f=8))  # foo(10, 20, 30, 40, 8)
