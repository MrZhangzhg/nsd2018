class Vendor:
    def __init__(self, phone, email):
        self.phone = phone
        self.email = email

    def send_email(self):
        print('Send email to %s' % self.email)

class BearToy:
    def __init__(self, name, size, color, phone, email):
        self.name = name
        self.size = size
        self.color = color
        self.vendor = Vendor(phone, email)

    def sing(self):
        print('I am %s, lalala...' % self.name)

if __name__ == '__main__':
    tidy = BearToy('tidy', 'middle', 'yellow', '400-123-8899', 'admin@tedu.cn')
    tidy.vendor.send_email()
