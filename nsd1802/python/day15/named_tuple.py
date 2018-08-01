from collections import namedtuple

u1 = ('bob', 25, 'bob@tedu.cn')
u1[0]

user = namedtuple('user', ['name', 'age', 'email'])
u2 = user('alice', 23, 'alice@tarena.com')
print(u2[1])
print(u2[1:])
print(u2.email)
