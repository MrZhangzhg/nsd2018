def func1(*args):  # 表示args是个元组
    print(args)

def func2(**kwargs):  # 表示kwargs是个字典
    print(kwargs)

def func3(*args, **kwargs):
    pass

if __name__ == '__main__':
    func1()
    func1('hao')
    func1('hao', 123)
    func1('hao', 123, 'hello')
    func2()
    func2(name='zhangsan')
    func2(name='zhangsan', age=23)
    func3(10, 'ehllo', name='bobo', age=20)
