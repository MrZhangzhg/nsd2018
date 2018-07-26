import string
from random import choice

all_chs = string.ascii_letters + string.digits
result = ['%s' % choice(all_chs) for i in range(8)]
print(''.join(result))
