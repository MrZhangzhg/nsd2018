class BearToy:
    def __init__(self, nm, size, color):  # 构造器函数，实例化时自动调用
        self.name = nm
        self.size = size   # 实例自动成为第一个参数，传递给self
        self.color = color  # 属性绑定在实例身上，实例在，属性就可以用
    def sing(self):
        print("I'am %s, lalala..." % self.name)

if __name__ == '__main__':
    tidy = BearToy('Tidy', 'Middle', 'White')  # 实例化
    print(tidy.size, tidy.color)
    big_bear = BearToy('熊大', 'Large', 'Brown')
    print(big_bear.size, big_bear.color)
    tidy.sing()
    big_bear.sing()
