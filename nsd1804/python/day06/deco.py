def deco(func):
    def color():
        return "\033[31;1m%s\033[0m" % func()
    return color

def welcome():
    return 'Hello World!'

@deco
def hello():
    return 'Hello China!'

if __name__ == '__main__':
    # a = deco(welcome)
    # print(a())
    welcome = deco(welcome)
    print(welcome())
    print(hello())  # 有装饰器表达的含义和上面两个语句一样
    # 将hello当作deco的参数传进去，返回color函数，再调用color函数
