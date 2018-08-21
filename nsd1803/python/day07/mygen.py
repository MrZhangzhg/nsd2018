def mygen():
    yield 'hello world'
    a = 10 + 20
    yield a
    yield [10, 20]

if __name__ == '__main__':
    a = mygen()
    for item in a:
        print(item)

    for item in a:
        print(item)

