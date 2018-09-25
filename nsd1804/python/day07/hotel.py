class Hotel:
    def __init__(self, room=200, cf=1.0, br=15):
        self.room = room
        self.cf = cf
        self.br = br

    def cacl(self, days=1):  # days只是函数的局部变量，函数调用完毕，days消失
        return (self.room * self.cf + self.br) * days

if __name__ == '__main__':
    std_room = Hotel()
    big_bed = Hotel(room=230, cf=0.9)
    print(std_room.cacl())
    print(std_room.cacl(2))
    print(big_bed.cacl())
    print(big_bed.cacl(2))
