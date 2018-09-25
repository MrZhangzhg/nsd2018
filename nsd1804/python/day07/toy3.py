class BearToy:
    def __init__(self, nm, size, color):  # 构造器函数，实例化时自动调用
        self.name = nm
        self.size = size   # 实例自动成为第一个参数，传递给self
        self.color = color  # 属性绑定在实例身上，实例在，属性就可以用
    def sing(self):
        print("I'am %s, lalala..." % self.name)

class NewBearToy(BearToy):  # 新的类是BearToy的子类
    def __init__(self, nm, size, color, material):
        # BearToy.__init__(self, nm, size, color)
        super(NewBearToy, self).__init__(nm, size, color)  # 推荐写法，与上一条一样的作用
        self.material = material
    def run(self):
        print('Running...')
    def sing(self):
        print("Wow~~~")

if __name__ == '__main__':
    b1 = NewBearToy('熊二', 'Large', 'Brown', 'Cotton')
    print(b1.material)
    b1.sing()
    b1.run()
