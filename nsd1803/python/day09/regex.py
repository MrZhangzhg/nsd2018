import re

re.match('f..', 'food')  # 匹配到，返回匹配对象
print(re.match('f..', 'seafood'))  # 匹配不到，返回None
m = re.search('f..', 'seafood')  # 从任意位置匹配，match从开头匹配
print(m.group())  # 返回匹配到的字符串
re.findall('f..', 'seafood is food')  # 返回所有匹配到的字符串列表
# 返回由匹配对象构成的迭代器，迭代器中的每个对象都有group方法
for m in re.finditer('f..', 'seafood is food'):
    print(m.group())

re.split('-|\.', 'hello-world-aaa.tar.gz')  # 切割成单词列表
# 把最后字符串中的X，替换成zzg
re.sub('X', 'zzg', 'hi X. How are you, X?')

patt = re.compile('f..')  # 如果有大量匹配，先将模式编译会有更好的执行效率
patt.search('seafood')  # 编译后的对象也有search/match等方法
m = patt.search('seafood')
m.group()
