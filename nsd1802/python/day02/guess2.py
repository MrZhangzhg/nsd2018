import random

num = random.randint(1, 10)
running = True

while running:
    answer = int(input('guess the number: '))
    if answer > num:
        print('猜大了')
    elif answer < num:
        print('猜小了')
    else:
        print('猜对了')
        running = False
