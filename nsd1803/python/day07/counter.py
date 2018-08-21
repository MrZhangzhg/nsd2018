def couter(start=0):
    count = start
    def incr():
        nonlocal count  # count既不是局部的，也不是全局的
        count += 1  # count = count + 1
        return count
    return incr  # 外层函数的返回值是内层函数

if __name__ == '__main__':
    a = couter()  # 调用函数，返回的是函数incr，所以a也是函数
    print(a())
    print(a())
    b = couter(10)
    print(b())
    print(b())
    print(a())
    print(b())
