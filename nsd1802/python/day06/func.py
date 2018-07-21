def func(n):  # 5
    if n == 1:
        return n
    return n * func(n - 1)
         # 5 * func(4)
         # 5 * 4 * func(3)
         # 5 * 4 * 3 * func(2)
         # 5 * 4 * 3 * 2 * func(1)
         # 5 * 4 * 3 * 2 * 1

if __name__ == '__main__':
    print(func(5))
    print(func(6))
