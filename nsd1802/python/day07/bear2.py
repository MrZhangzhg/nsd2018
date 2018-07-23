class Vendor:
    def __init__(self, phone, email):
        self.phone = phone
        self.email = email

    def call(self):
        print('calling %s' % self.phone)

class BearToy:
    def __init__(self, color, size, phone, email):
        self.color = color  # 绑定属性到实例
        self.size = size
        self.vendor = Vendor(phone, email)

if __name__ == '__main__':
    bigbear = BearToy('Brown', 'Middle', '4008009999', 'sales@tedu.cn')
    print(bigbear.color)
    bigbear.vendor.call()
