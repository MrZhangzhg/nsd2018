alist = [10, 20, 30, 'bob', 'alice', [1,2,3]]
len(alist)
alist[-1]  # 取出最后一项
alist[-1][-1]  # 因为最后一项是列表，列表还可以继续取下标
[1,2,3][-1]  # [1,2,3]是列表，[-1]表示列表最后一项
alist[-2][2]  # 列表倒数第2项是字符串，再取出字符下标为2的字符
alist[3:5]   # ['bob', 'alice']
10 in alist  # True
'o' in alist  # False
100 not in alist # True
alist[-1] = 100  # 修改最后一项的值
alist.append(200)  # 向列表中追加一项



