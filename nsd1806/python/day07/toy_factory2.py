class Vendor:
    def __init__(self, em, ph):
        self.email = em
        self.phone = ph

class BearToy:
    def __init__(self, name, size, color, em, ph):
        '实例化时，自动调用'
        self.name = name  # 绑定属性到self上，整个类中都可引用
        self.size = size
        self.color = color
        self.vendor = Vendor(em, ph)

    def sing(self):
        print('I am %s, Lalala...' % self.name)

if __name__ == '__main__':
    big = BearToy('熊大', 'Large', 'Brown', 'admin@tedu.cn', '4001001234')  # 将会调用__init__方法，big传递给self
    print(big.vendor.phone)
