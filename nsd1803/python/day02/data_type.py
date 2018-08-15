# bool类型也是整型
True + 2  # 3
False * 5  # 0
0o11  # 8进制的11
0x11  # 16进制的11
0b11  # 2进制的11
# 修改文件的权限从644到755

import os
os.chmod('data_type.py', 755)  # 不正常，因为权限是8进制数
os.chmod('data_type.py', 0o755)

print('tom\'s pet is cat')
print("tom's pet is cat")
names = '''耿永强
何文
陈宝
'''
print(names)

py_str = 'python'
print(len(py_str))  # 字符串长度
py_str[0]  # 取出第一个字符，[]中的数字称作索引，或下标
# py_str[6]  # 错误，下标越界
py_str[len(py_str) - 1]  # py_str[5]，取最后一项
py_str[-1]  # 最后一项的下标是-1
py_str[-len(py_str)]  # 最左一项是-6
py_str[2:4]  # 切片，2对应的t包含，4对应的o不包含，所以结果是th
py_str[2:6]  # 切片没有的下标，不会报错
py_str[2:60]  # 同上
py_str[2:]  # 结尾不写，表示到取到结束部分
py_str[0:2]  # py
py_str[:2]  # py
py_str[:]  # python
py_str[::2]  # 2表示步长值，pto
py_str[1::2]  # yhn
py_str[::-1]  # 步长值为负，表示从右向左取值

py_str + ' is good'
'*' * 50
't' in py_str  # True
'th' in py_str  # True
'to' in py_str   # False
'to' not in py_str  # True
###############################################
alist = ['bob', 'alice', 10, 20, [1, 2, 3]]
len(alist)
alist[:2]
'bob' in alist  # True
3 in alist  # False
3 in alist[-1]  # True，因为alist[-1]也是列表，相当于下面代码
3 in [1, 2, 3]
alist[-1][1]  # 取出2
['tom'] + alist  # ['tom']是列表，列表中只有一个项目
alist * 2
alist.append(100)  # 向列表追加元素
##########################################
atuple = ('bob', 'alice', 10, 20)  # 元组可以认为是静态的列表
atuple[2:]
10 in atuple
(100, 200) + atuple
# (100) + atuple  # 错误，单元素元组必须有逗号，否则小括号会自动剥离
(100,) + atuple
#############################
# 字典是key-value对的形式，key不能重复
adict = {'name': 'zhangsan', 'age': 25}
25 in adict  # False
'age' in adict  # True
adict['name']  # 'zhangsan'



















