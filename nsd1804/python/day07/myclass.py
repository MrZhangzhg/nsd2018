class A:
    def foo(self):
        print('in A-foo')
    def sing(self):
        print('lalala...')

class B:
    def bar(self):
        print('in B-bar')
    def sing(self):
        print('wow~~~')

class C(B, A):  # 类可以有多个父类（基类）
    pass

if __name__ == '__main__':
    c = C()
    c.foo()
    c.bar()
    c.sing()  # 父子类有同名方法时，查找自下向上，自左向右
