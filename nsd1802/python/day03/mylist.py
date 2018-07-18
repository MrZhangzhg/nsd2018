# 10+5的结果放到列表中
[10 + 5]
# 10+5这个表达式计算10次
[10 + 5 for i in range(10)]
# 10+i的i来自于循环
[10 + i for i in range(10)]
[10 + i for i in range(1, 11)]
# 通过if过滤，满足if条件的才参与10+i的运算
[10 + i for i in range(1, 11) if i % 2 == 1]
[10 + i for i in range(1, 11) if i % 2]
# 生成IP地址列表
['192.168.1.%s' % i for i in range(1, 255)]
