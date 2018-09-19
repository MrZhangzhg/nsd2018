alist = ['zhangsan', 'lisi', 'wangwu']

for ind in range(len(alist)):
    print('%s: %s' % (ind, alist[ind]))

print(list(enumerate(alist)))
# [(0, 'zhangsan'), (1, 'lisi'), (2, 'wangwu')]

for item in enumerate(alist):
    print('%s: %s' % (item[0], item[1]))

for ind, val in enumerate(alist):
    print('%s: %s' % (ind, val))

print(list(reversed(alist)))
for name in reversed(alist):  # 翻转
    print(name)

print(sorted(alist))   # 排序



