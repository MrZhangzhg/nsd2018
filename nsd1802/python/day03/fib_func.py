def gen_fib(l):
    fib = [0, 1]

    for i in range(l - len(fib)):
        fib.append(fib[-1] + fib[-2])

    return fib  # 返回列表，不返回变量fib

a = gen_fib(10)
print(a)
print('-' * 50)
n = int(input("length: "))
print(gen_fib(n))  # 不会把变量n传入，是把n代表的值赋值给形参
