import time
import sys

l = 19
counter = 0
print('#' * (l + 1), end='')


while True:
    sys.stdout.flush()
    try:
        time.sleep(0.2)
    except KeyboardInterrupt:
        print()
        break
    print('\r%s@%s' % ('#' * counter, '#' * (l - counter)), end='')
    counter += 1
    if counter > l:
        counter = 0
