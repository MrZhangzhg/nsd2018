alist = [1, 50, 60, 100]
alist[0] = 10
alist[1:3] = [30, 40]
alist[3:3] = [50, 60, 70, 80, 90]
alist.append(30)
alist.sort()
alist.reverse()
alist.count(30)  # 统计30出现的次数
alist.remove(30)
alist.pop()  # 默认弹出最后一项
alist.pop(2)
alist.extend('abc')
alist.extend(['abc', 'xyz'])
alist.index(50)  # 50的下标
alist.insert(3, 1000)  # 把1000放到下标为3的位置


