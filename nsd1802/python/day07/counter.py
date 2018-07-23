def counter(start=0):
    count = start
    def incr():
        nonlocal count
        count += 1
        return count
    return incr

if __name__ == '__main__':
    a = counter()
    print(a())
    b = counter(10)
    print(b())
    print(a())
    print(b())

