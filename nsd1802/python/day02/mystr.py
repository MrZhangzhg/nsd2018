sentence = 'tom\'s pet is a cat'
sentence2 = "tom's pet is a cat"
sentence3 = "tom said:\"hello world!\""
sentence4 = 'tom said:"hello world"'
# 三个连续的单引号或双引号，可以保存输入格式
words = """
hello
world
abcd"""
print(words)

py_str = 'python'
len(py_str)  # 取长度
py_str[0]  # 第一个字符
'python'[0]
py_str[-1]  # 最后一个字符
# py_str[6]  # 错误，下标超出范围
py_str[2:4]  # 切片，起始下标包含，结束下标不包含
py_str[2:]  # 从下标为2的字符取到结尾
py_str[:2]  # 从开头取到下标是2之前的字符
py_str[:]  # 取全部
py_str[::2]  # 步长值为2，默认是1
py_str[1::2]  # 取出yhn
py_str[::-1]  # 步长为负，表示自右向左取

py_str + ' is good'  # 简单的拼接到一起
py_str * 3  # 把字符串重复3遍

't' in py_str  # True
'th' in py_str  # True
'to' in py_str  # False
'to' not in py_str  # True






