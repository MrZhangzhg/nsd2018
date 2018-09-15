if 3 > 10:
    print('yes')
    print('ok')
else:
    print('no')

# 任何非0数字都是True，值为0是False
if -0.0:
    print('yes')

if 0.1:
    print('0.1 yes')

# 任何非空对象都是True，空是False: []/()/{}/''
if ' ':
    print('space ok')
#####################################

a = 10
b = 20
if a < b:
    smaller = a
else:
    smaller = b
print(smaller)

s = a if a < b else b
print(s)

