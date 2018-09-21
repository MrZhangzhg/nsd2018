def myfunc(*args):  # *args表示args是元组
    print(args)

def myfunc2(**kwargs):  # **kwargs表示kwargs是字典
    print(kwargs)

if __name__ == '__main__':
    myfunc()
    myfunc('hao')
    myfunc('hao', 123)
    myfunc('hao', 123, 'zhangsan')
    myfunc2()
    myfunc2(name='zhangsan')
    myfunc2(name='zhangsan', age=20)
