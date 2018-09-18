def gen_fib(l=10):
    fib = [0, 1]

    for i in range(l - 2):
        fib.append(fib[-1] + fib[-2])

    return fib

print(gen_fib())
print(gen_fib(20))
