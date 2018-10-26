import os

print('hello world!')
pid = os.fork()
if pid:
    print('hello from parent')
else:
    print('hello from child')

print('hello from both')
