import random

result = random.randint(1, 10)
counter = 0

while counter < 3:
    answer = int(input("guess the number: "))
    if answer > result:
        print('猜大了')
    elif answer < result:
        print('猜小了')
    else:
        print('猜对了')
        break
    counter += 1
else:  # 当循环正常结束时，else子句执行，如果是被break掉的，就不执行了
    print(result)
