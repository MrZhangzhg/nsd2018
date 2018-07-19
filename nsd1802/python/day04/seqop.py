from random import randint

alist = list()  # []
list('hello')  # ['h', 'e', 'l', 'l', 'o']
list((10, 20, 30))  # [10, 20, 30]  元组转列表
astr = str()  # ''
str(10)  # '10'
str(['h', 'e', 'l', 'l', 'o'])  # 将列表转成字符串
atuple = tuple()  # ()
tuple('hello')  # ('h', 'e', 'l', 'l', 'o')
num_list = [randint(1, 100) for i in range(10)]
max(num_list)
min(num_list)
