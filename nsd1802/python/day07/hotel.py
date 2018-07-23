class Hotel:
    def __init__(self, price=200, cutoff=1.0, br=15):
        self.price = price
        self.cutoff = cutoff
        self.br = br

    def calc(self, days=1):
        return (self.price * self.cutoff + self.br) * days

if __name__ == '__main__':
    stdroom = Hotel()
    bigbed = Hotel(220, 0.9)
    print(stdroom.calc())
    print(stdroom.calc(2))
    print(bigbed.calc())
    print(bigbed.calc(2))
