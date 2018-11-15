class BearToy:
    def __init__(self, name, size, color):
        '实例化时，自动调用'
        self.name = name  # 绑定属性到self上，整个类中都可引用
        self.size = size
        self.color = color

    def sing(self):
        print('I am %s, Lalala...' % self.name)

class NewBearToy(BearToy):  # 新类是BearToy的子类
    def __init__(self, name, size, color, date):
        '父子类有同名方法，子类对象执行子类方法'
        # BearToy.__init__(self, name, size, color)
        super(NewBearToy, self).__init__(name, size, color)
        self.date = date

    def run(self):
        print('我能跑了!')

if __name__ == '__main__':
    big = NewBearToy('倒霉熊', '小号', '白', '2018-10-1')  # 将会调用__init__方法，big传递给self
    big.sing()
    big.run()
