def colors(func):
    def set_color():
        return '\033[31;1m%s\033[0m' % func()
    return set_color

@colors
def hello():
    return 'Hello World!'

@colors
def welcome():
    return 'How are you?'

if __name__ == '__main__':
    print(hello)  # 因为有装饰器，此处不是调用hello函数，而是将hello
                    # 作为colors的参数
    print(hello())  # ()实际上是对set_color的调用
    print(welcome())

