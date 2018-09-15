import random

number = random.randint(1, 100)
counter = 0

while counter < 3:
    answer = int(input('guest the number: '))
    if answer > number:
        print('猜大了')
    elif answer < number:
        print('猜小了')
    else:
        print('猜对了')

    counter += 1
