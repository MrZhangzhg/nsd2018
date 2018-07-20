# 集合相当于是无值的字典，所以也用{}表示
myset = set('hello')
len(myset)
for ch in myset:
    print(ch)

aset = set('abc')
bset = set('cde')
aset & bset  # 交集
aset.intersection(bset)  # 交集
aset | bset  # 并集
aset.union(bset)  # 并集
aset - bset  # 差补
aset.difference(bset)  # 差补
aset.add('new')
aset.update(['aaa', 'bbb'])
aset.remove('bbb')
cset = set('abcde')
dset = set('bcd')
cset.issuperset(dset)  # cset是dset的超集么？
cset.issubset(dset)  # cset是dset的子集么？


