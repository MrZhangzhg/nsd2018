class BearToy:
    def __init__(self, name, size, color):  # 在实例化时自动执行
        self.name = name
        self.size = size
        self.color = color

    def sing(self):
        print('I am %s, lalala...' % self.name)

if __name__ == '__main__':
    # 把参数传给__init__, 实例本身，如tidy，自动作为第一个参数传递
    tidy = BearToy('tidy', 'middle', 'yellow')
    print(tidy.size)
    print(tidy.color)
    tidy.sing()
