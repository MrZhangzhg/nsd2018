import random

num = random.randint(1, 10) # 随机生成1－10之间的数字
answer = int(input('guess a number: '))  # 将用户输入的字符转成整数
if answer > num:
    print('猜大了')
elif answer < num:
    print('猜小了')
else:
    print('猜对了')

print('the number:', num)
