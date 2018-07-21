def func1(*args):  # *表示args是个元组
    print(args)

def func2(**kwargs):  # **表示kwargs是个字典
    print(kwargs)

def func3(x, y):
    print(x * y)

def func4(name, age):
    print("%s is %s years old" % (name, age))

if __name__ == '__main__':
    func1()
    func1(10)
    func1(10, 'bob')
    func2()
    func2(name='bob', age=25)
    func3(*[10, 5])  # 调用的时候，*表示拆开后面的数据类型
    func4(**{'name': 'bob', 'age': 25})  # name='bob', age=25
