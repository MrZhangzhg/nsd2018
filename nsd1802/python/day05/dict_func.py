adict = dict([('name', 'bob'),('age', 25)])
len(adict)
hash(10)  # 判断给定的数据是不是不可变的，不可变数据才能作为key
adict.keys()
adict.values()
adict.items()
# get方法常用，重要
adict.get('name')  # 取出字典中name对应的value，如果没有返回None
print(adict.get('qq'))  # None
print(adict.get('qq', 'not found'))  # 没有qq，返回指定内容
print(adict.get('age', 'not found'))
adict.update({'phone': '13455667788'})
