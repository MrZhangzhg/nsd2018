def get_info(name, age):
    print('%s is %s years old' % (name, age))

if __name__ == '__main__':
    get_info('bob', 25)
    get_info(25, 'bob')  # 能运行，语义不对
    get_info(age=25, name='bob')
    # get_info()  # Error
    # get_info('bob', 25, 30)  # Error
    # get_info(age=25, 'bob')  # key=val的形式必须出现在后面
    # get_info(25, name='bob') # 25按参数顺序传递给name，又赋值bob给name
    get_info('bob', age=25)
