result = 0
counter = 0

while counter < 100:
    counter += 1
    # if counter % 2:  # 求余，只有1和0两种情况 ，1是True，0是False
    if counter % 2 == 1:
        continue
    result += counter

print(result)
