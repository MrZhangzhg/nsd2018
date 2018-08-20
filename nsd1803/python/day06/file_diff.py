# cp /etc/passwd /tmp
# cp /etc/passwd /tmp/mima
# 修改第二个文件，与第一个文件有些行不一样
f1 = open('/tmp/passwd')
f2 = open('/tmp/mima')
f3 = open('/tmp/result', 'w')
s1 = set(f1)
s2 = set(f2)
f3.writelines(s2 - s1)
f1.close()
f2.close()
f3.close()
