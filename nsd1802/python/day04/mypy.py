#!/usr/bin/env python3


import keyword
keyword.kwlist  # 关键字列表
keyword.iskeyword('pass')  # 判断pass是不是关键字

a = b = 10
a = 20  # b的值不变，因为数字是不可变的

alist = blist = [1, 2]
alist[0] = 10  # blist也会改变，因为列表是可变的


