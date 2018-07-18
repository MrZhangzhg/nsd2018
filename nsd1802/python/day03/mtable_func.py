def mtable(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print('%s*%s=%s' % (j, i, i * j), end=' ')
        print()

mtable(6)
mtable(9)
