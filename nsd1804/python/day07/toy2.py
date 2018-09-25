class Vendor:
    def __init__(self, phone, email):
        self.phone = phone
        self.email = email

class BearToy:
    def __init__(self, nm, size, color, phone, email):
        self.name = nm
        self.size = size
        self.color = color
        self.vendor = Vendor(phone, email)  # Vendor的实例
    def sing(self):
        print("I'am %s, lalala..." % self.name)

if __name__ == '__main__':
    tidy = BearToy('Tidy', 'middle', 'White', '400-100-8989', 'admin@tedu.cn')
    print(tidy.vendor.phone)
    tidy.sing()
