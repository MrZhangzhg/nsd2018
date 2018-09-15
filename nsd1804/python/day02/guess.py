import random

number = random.randint(1, 100)  # 随机生成1到5之间的数字
print(number)
# answer = input('guess the number: ')   # '3'
# answer = int(answer)   # int('3')
answer = int(input('guest the number: '))
if answer > number:
    print('猜大了')
elif answer < number:
    print('猜小了')
else:
    print('猜对了')
