adict = {'name': 'bob', 'age': 23}

print('bob' in adict)  # bob是字典的key么？
print('name' in adict)  # True
print(len(adict))  # 2
for key in adict:
    print('%s: %s' % (key, adict[key]))
print('%(name)s: %(age)s' % adict)
