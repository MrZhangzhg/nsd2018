def foo():
    print('in foo')
    bar()

# foo()

def bar():
    print('in bar')

if __name__ == '__main__':
    foo()
