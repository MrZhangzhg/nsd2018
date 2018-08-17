for i in range(1, 10):  # 外层循环控制行
    for j in range(1, i + 1):  # 内层循环控制某一行
        print('%sX%s=%s' % (j, i, j * i), end=' ')
    print()

