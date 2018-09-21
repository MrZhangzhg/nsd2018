# def foo():
#     def bar():
#         print('hello world!')
#     return bar
#
# if __name__ == '__main__':
#     a = foo()
#     a()
###############################
# def foo(word):
#     def bar():
#         print('hello %s!' % word)
#     return bar
#
# if __name__ == '__main__':
#     a = foo('xixi')
#     a()
#     b = foo('haha')
#     b()
###############################
def counter(start=0):
    count = start
    def incr():
        # 为了把外层函数的变量在内层函数中引用，需要使用关键字nonlocal
        nonlocal count  # count不是incr的局部变量，它也不是全局，使用nonlocal才能应用
        count += 1
        return count
    return incr  # 外层函数的返回值是内层函数

if __name__ == '__main__':
    a = counter()  # a本质上是函数incr
    print(a())   # 执行incr()
    b = counter(10)
    print(b())
    print(a())
    print(b())














