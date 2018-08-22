class Hotel:
    def __init__(self, basic=200, cf=1.0, br=15):
        self.basic = basic
        self.cutoff = cf
        self.br = br

    def calc(self, days=1):
        return (self.basic * self.cutoff + self.br) * days

if __name__ == '__main__':
    stdroom = Hotel()
    print(stdroom.calc())
    print(stdroom.calc(2))
    bigbed = Hotel(basic=230, cf=0.9)
    print(bigbed.calc())
    print(bigbed.calc(2))
