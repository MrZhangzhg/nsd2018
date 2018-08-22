class BearToy:
    def __init__(self, name, size, color):
        self.name = name
        self.size = size
        self.color = color

    def sing(self):
        print('I am %s, lalala...' % self.name)

class NewBear(BearToy):  # 父类，也叫基类，是BearToy
    def run(self):
        print('running...')

if __name__ == '__main__':
    b1 = NewBear('big_bear', 'Large', 'Brown')
    b1.sing()
    b1.run()
