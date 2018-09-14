# 如果希望将数据输出在屏幕上，常用的方法是print
print('Hello World!')
print('Hello' + 'World!')
print('Hello', 'World!')  # 默认各项之间用空格分隔
print('Hello', 'World!', 'abc', sep='***')  # 指定分隔符是***
print('Hello World!', end='####')
# print默认在打印结束后加上一个回车，可以使用end=重置结束符

n = input('number: ')  # 屏幕提示number:  用户输入的内容赋值给n
print(n)  # input得到的数据全都是字符类型
# a = n + 10   # 错误，不能把字符和数字进行运算
a = int(n) + 10  # int可以将字符串数值转成相应的整数
print(a)
b = n + str(10)  # str可以将其他数据转换成字符
print(b)

