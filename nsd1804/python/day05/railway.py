import time

print('#' * 20, end='')
counter = 0

while True:
    print('\r%s@%s' % ('#' * counter, '#' * (19 - counter)), end='')
    counter +=1
    if counter == 20:
        counter = 0
    time.sleep(0.3)
