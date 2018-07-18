for i in range(1, 10):
    for j in range(1, i + 1):
        print('%s*%s=%s' % (j, i, i * j), end=' ')
    print()

# i=1 ->j: [1]
# i=2 ->j: [1,2]
# i=3 ->j: [1,2,3]
