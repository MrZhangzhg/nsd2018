def mygen():
    yield 'hello'
    a = 10 + 20
    yield a
    yield [1, 2, 3]

if __name__ == '__main__':
    m = mygen()
    for i in m:
        print(i)

    for i in m:
        print(i)  # 无值，因为生成器对象只能用一次


