# adict = dict(['ab', 'cd', ('name', 'zhangsan')])
# print(adict)

bdict = {}.fromkeys(['bob', 'alice', 'tom'], 7)
print(bdict)
for key in bdict:
    print('%s: %s' % (key, bdict[key]))

print('%(bob)s' % bdict)

bdict['tom'] = 8  # tom已经是字典的key，更新值
bdict['john'] = 6  # john没在字典中，新增一项
print(bdict)
bdict.pop('alice')
7 in bdict  # 返回False
'tom' in bdict  # 返回True

cdict = bdict.copy()  # 将bdict的内容赋值给cdict，cdict使用全新的内存空间
bdict.get('bob')  # 返回bob对应的value，如果没有bob，默认返回None
bdict.get('jane', 'not found')  # 如果没有jane，返回not found
bdict.setdefault('bob', 10)  # bob已经是字典的key，返回value
bdict.setdefault('jane', 10)  # jane没在字典中，向字典中写入
list(bdict.keys())
list(bdict.values())
list(bdict.items())
bdict.update({'aaa': 111, 'bbb': 222})  # 合并字典



