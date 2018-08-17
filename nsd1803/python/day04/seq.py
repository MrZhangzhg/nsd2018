list('abcd')
list((10, 20, 30))
tuple('abcd')
str(100)
str((10, 20, 30))
max([10, 200, 30])
min([10, 200, 30])
max('hello')

users = ['bob', 'alice', 'john']
for i in range(len(users)):  # [0, 1, 2]
    print('#%s: %s' % (i, users[i]))

list(enumerate(users))  # 应用时不必转换
for item in enumerate(users):
    print('#%s: %s' % (item[0], item[1]))

for ind, user in enumerate(users):  # (0, bob), (1, alice)
    print('#%s: %s' % (ind, user))

for u in reversed(users):
    print(u)

sorted(users)

# 字符编码：ASCII, ISO8859-1/Latin1, GB2312/GBK/GB18030,
# ISO -> utf8
# 0b1100001 -> a; 0b1100010 -> b;


