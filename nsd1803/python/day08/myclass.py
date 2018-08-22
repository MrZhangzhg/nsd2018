class A:
    def foo(self):
        print('in A-foo')

class B:
    def bar(self):
        print('in B-bar')

class C(A, B):
    pass

if __name__ == '__main__':
    c = C()
    c.foo()
    c.bar()
