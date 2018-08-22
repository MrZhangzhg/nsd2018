class BearToy:
    def __init__(self, name, size, color):
        self.name = name
        self.size = size
        self.color = color

    def sing(self):
        print('I am %s, lalala...' % self.name)

class NewBear(BearToy):
    def __init__(self, name, size, color, material):
        # BearToy.__init__(self, name, size, color)
        super(NewBear, self).__init__(name, size, color)
        self.material = material

    def run(self):
        print('running...')

if __name__ == '__main__':
    b1 = NewBear('big_bear', 'Large', 'Brown', 'cotton')
    b1.sing()
    b1.run()
