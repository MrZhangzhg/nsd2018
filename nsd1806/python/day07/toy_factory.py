class BearToy:
    def __init__(self, name, size, color):
        '实例化时，自动调用'
        self.name = name  # 绑定属性到self上，整个类中都可引用
        self.size = size
        self.color = color

    def sing(self):
        print('I am %s, Lalala...' % self.name)

if __name__ == '__main__':
    big = BearToy('熊大', 'Large', 'Brown')  # 将会调用__init__方法，big传递给self
    second = BearToy('熊二', 'Middle', 'Brown')
    print(big.size)
    print(big.color)
    big.sing()
    second.sing()
