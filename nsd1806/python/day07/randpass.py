from string import ascii_letters, digits
from random import choice

all_chs = ascii_letters + digits

def randpass(n=8):
    result = [choice(all_chs) for i in range(n)]
    return ''.join(result)

if __name__ == '__main__':
    print(randpass())
    print(randpass(10))
