result = 0  # 变量使用前必须先赋值
counter = 1

while counter < 101:
    result += counter
    counter += 1

print(result)

# result = result + counter  -> reuslt:1
# counter = counter + 1  -> counter: 2
# result = result + counter  -> result:3


