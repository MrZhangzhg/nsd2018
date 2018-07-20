import time

length = 19
count = 0

while True:
    print('\r%s@%s' % ('#' * count, '#' * (length - count)), end='')
    try:
        time.sleep(0.3)
    except KeyboardInterrupt:
        print('\nBye-bye')
        break
    if count == length:
        count = 0
    count += 1
