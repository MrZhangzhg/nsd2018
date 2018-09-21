def myfunc(name, age):
    print('%s is %s years old' % (name, age))

if __name__ == '__main__':
    user = ['bob', 20]
    user2 = {'name': 'alice', 'age': 18}
    myfunc(*user)  # *user表示把user拆开
    myfunc(**user2)  # 拆成name='alice' age=18
