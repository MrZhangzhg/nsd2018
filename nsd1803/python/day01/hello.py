# 美胜丑，明胜暗，简胜繁
# print('Hello World!')  # 字符串必须放到引号中
# print('Hello', 'World', '!', 123)  # 数字不用放到引号中
# print('Hello', 'World', '!', 123, sep='***')  # 各项间用***分开
# print('Hello' + 'World!')  # 字符串拼接
# print('Hello', 'World', '!', 123, end='')  # 不打印回车


user = input('username: ')
print(user)

a = input('number: ')  # input读入的数据都是字符类型
# a + 5   # 错误，不能把数字和字符进行加法运算
print(int(a) + 5)  # 将字符转换成数字，再和5进行加法运算
print(a + str(5))  # 将数字5转换成字符，再和字符串拼接

