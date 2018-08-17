def gen_fib(l):
    fib = [0, 1]

    for i in range(l - len(fib)):
        fib.append(fib[-1] + fib[-2])

    return fib  # 函数如果没有return，默认返回None
                # 返回值是把fib代表的列表返回，不会把变量名fib返回

print(gen_fib(10))
l = int(input('length: '))
alist = gen_fib(l)  # 传参是把l代表的值传进去，不会把名字l传进去
mylist = [10 + i for i in alist]
print(mylist)
