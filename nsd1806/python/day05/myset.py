a = set('abc')
b = set('bcd')
c = set(['abc', 123, 'hello'])
for item in c:
    print(item)
a & b  # 交集
a | b  # 并集
a - b  # 差补，仅在a中存在的元素
c.add('greet')
c.update(['ni', 'hao'])
c.remove(123)
a.intersection(b)   # a & b
a.union(b)   # a | b
a.difference(b)   # a - b

# cp /etc/passwd /tmp
# cp /etc/passwd /tmp/mima
# 修改/tmp/mima和/tmp/passwd，令两个文件有些不同
with open('/tmp/passwd') as fobj:
    aset = set(fobj)

with open('/tmp/mima') as fobj:
    bset = set(fobj)

print(aset)
print('-' * 30)
print(bset)

with open('/tmp/newfile', 'w') as fobj:
    fobj.writelines(bset - aset)




