def color(func):
    def red(*args):
        return '\033[31;1m%s\033[0m' % func(*args)
    return red

@color
def hello(word):
    return 'Hello %s!' % word

@color
def welcome():
    return 'How are you?'

if __name__ == '__main__':
    print(hello('China'))
    print(welcome())
