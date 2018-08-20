# 集合也用{}表示，就像是一个无值的字典

s1 = set('abc')
s2 = set('bcd')
len(s1)
for ch in s1:
    print(ch)
'a' in s1
s1 | s2  # 取并集
s1 & s2  # 取交集
s1 - s2  # 取差补，s1中有但s2中没有的元素
s1.add(10)
s1.update(['hello', 'world'])
s1.remove(10)
s1.issubset(s2)  # s1是s2的子集吗
s1.issuperset(s2)  # s1是s2的超集吗
s1.union(s2)  # s1 | s2
s1.intersection(s2)  # s1 & s2
s1.difference(s2)  # s1 - s2
