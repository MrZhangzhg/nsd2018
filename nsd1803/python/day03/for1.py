astr = 'abc'
alist = ['bob', 'alice']
atuple = (10, 20, 30)
adict = {'name': '王凯', 'age': 22}

for ch in astr:
    print(ch)

for name in alist:
    print(name)

for i in atuple:
    print(i)

for key in adict:
    print('%s: %s' % (key, adict[key]))

list(range(10))  # 只写10，表示结束数字是10，但是不包含10。开始数字是0
list(range(6, 11))  # [6, 7, 8, 9, 10]
list(range(1, 10, 2))  # [1, 3, 5, 7, 9]
list(range(10, 0, -1))  # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

for i in range(3):
    print('hello')

sum100 = 0
for i in range(1, 101):
    sum100 += i
print(sum100)

s = 0
for i in range(1, 101, 2):
    s += i
print(s)














