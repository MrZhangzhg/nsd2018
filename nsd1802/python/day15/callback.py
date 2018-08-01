def foo(func, *args):
    print 'processing...'
    func(*args)

def loop(num):
    for i in range(num):
        print i

if __name__ == '__main__':
    foo(loop, 10)
