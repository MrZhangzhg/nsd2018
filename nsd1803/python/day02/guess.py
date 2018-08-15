import random

result = random.randint(1, 10)  # 生成1到10之间的一个整数，可以包括1或10
answer = int(input("guess the number: "))

if answer > result:
    print('猜大了')
elif answer < result:
    print('猜小了')
else:
    print('猜对了')

print(result)
