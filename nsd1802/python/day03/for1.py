astr = 'hello'
alist = [10, 20, 30]
atuple = ('bob', 'tom', 'alice')
adict = {'name': 'john', 'age': 23}

for ch in astr:
    print(ch)

for i in alist:
    print(i)

for name in atuple:
    print(name)

for key in adict:
    print('%s: %s' % (key, adict[key]))
