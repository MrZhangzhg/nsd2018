"%s is %s years old" % ('bob', 23)  # 常用
"%s is %d years old" % ('bob', 23)  # 常用
"%s is %d years old" % ('bob', 23.5)  # %d是整数 常用
"%s is %f years old" % ('bob', 23.5)
"%s is %5.2f years old" % ('bob', 23.5)  # %5.2f是宽度为5，2位小数
"97 is %c" % 97
"11 is %#o" % 11  # %#o表示有前缀的8进制
"11 is %#x" % 11
"%10s%5s" % ('name', 'age')  # %10s表示总宽度为10，右对齐, 常用
"%10s%5s" % ('bob', 25)
"%10s%5s" % ('alice', 23)
"%-10s%-5s" % ('name', 'age')  # %-10s表示左对齐, 常用
"%-10s%-5s" % ('bob', 25)
"%10d" % 123
"%010d" % 123

"{} is {} years old".format('bob', 25)
"{1} is {0} years old".format(25, 'bob')
"{:<10}{:<8}".format('name', 'age')








