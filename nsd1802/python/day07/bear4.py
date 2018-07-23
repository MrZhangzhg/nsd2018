class BearToy:
    def __init__(self, nm, color, size):
        self.name = nm
        self.color = color  # 绑定属性到实例
        self.size = size

    def sing(self):
        print('lalala...')

    def speak(self):
        print('My name is %s' % self.name)

class NewBear(BearToy):
    def __init__(self, nm, color, size, date):
        # BearToy.__init__(self, nm, color, size)
        super(NewBear, self).__init__(nm, color, size)
        self.date = date

    def run(self):
        print('running...')

if __name__ == '__main__':
    b1 = NewBear('venie', 'Brown', 'Small', '2018-07-20')
    b1.sing()
    b1.run()
