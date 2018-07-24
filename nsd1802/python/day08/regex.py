import re

m = re.match('f..', 'food')  # 匹配到返回对象
print(re.match('f..', 'seafood'))  # 匹配不到返回None
m.group()  # 返回匹配的值
m = re.search('f..', 'seafood')
m.group()
re.findall('f..', 'seafood is food')  # 返回所有匹配项组成的列表

result = re.finditer('f..', 'seafood is food')  # 返回匹配对象组成的迭代器
for m in result:  # 从迭代器中逐个取出匹配对象
    print(m.group())

re.sub('f..', 'abc', 'fish is food')
re.split('\.|-', 'hello-world.tar.gz')  # 用.和-做切割符号

patt = re.compile('f..')  # 先把要匹配的模式编译，提升效率
m = patt.search('seafood')  # 指定在哪个字符串中匹配
m.group()

