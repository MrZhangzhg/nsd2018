import string
from random import choice

all_chs = string.ascii_letters + string.digits
result = [choice(all_chs) for i in range(8)]
print(''.join(result))
