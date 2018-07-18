fib = [0, 1]

l = int(input('length: '))
for i in range(l - len(fib)):
    fib.append(fib[-1] + fib[-2])

print(fib)
