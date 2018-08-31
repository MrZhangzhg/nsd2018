'''
元组是序列类型的，它有下标，每一项没有名字。
命名的元组，可以为元组中的每一项起名，类似于字典的key
'''

import collections

p1 = (10, 20)
Point = collections.namedtuple('Point', ['x', 'y', 'z'])
# 注意：前面的Point和后面第一个字符串Point要求一致
p2 = Point(10, 30, 40)
p2[0]  # 像元组一样用下标来找到元素
p2[1]
p2[1:]  # 也可以切片
p2.x  # 也可以像OOP对象一样用 实例.属性
p2.y
p2.z


def a():
    pass

def b():
    pass

def c():
    pass

def call_func(func):
    func()

call_func(a)
call_func(b)






