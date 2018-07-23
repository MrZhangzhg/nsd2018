class A:
    def foo(self):
        print('in A foo')
    def hello(self):
        print('A hello')

class B:
    def bar(self):
        print('in B bar')
    def hello(self):
        print('B hello')

class C(B, A):
    pass
    # def hello(self):
    #     print('C hello')

if __name__ == '__main__':
    c = C()
    c.foo()
    c.bar()
    c.hello()
