[10]
[3 + 2]
[3 + 2 for i in range(10)]  # 执行10次3+2
[3 + i for i in range(10)]  # 循环控制3+i运行多少次
[3 + i for i in range(10) if i % 2 == 1]  # 判断条件作为过滤依据
['192.168.1.%s' % i for i in range(1, 255)]


