def set_color(func):
    def color():
        return "\033[31;1m%s\033[0m" % func()
    return color

def hello():
    return "Hello World!"

@set_color
def greet():
    return "How are you?"

if __name__ == '__main__':
    # hello = set_color(hello)
    # print(hello())
    print(greet)   # 此时调用set_color(greet)，返回color函数
    print(greet())   # 此时调用的是color()
