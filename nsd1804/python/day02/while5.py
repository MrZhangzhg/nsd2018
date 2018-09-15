result = 0
counter = 0

while counter < 100:
    counter += 1
    # if counter % 2:  # counter % 2结果不是0就是1，0为False，1为True
    if counter % 2 == 1:
        continue

    result += counter

print(result)
