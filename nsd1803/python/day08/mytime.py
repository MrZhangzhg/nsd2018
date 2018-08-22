class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def say_hi(self):  # 必须有实例，通过实例调用
        print('hello world!')

    @classmethod  # 类方法，没有实例就可以调用
    def create_date(cls, str_date):  # cls是类本身，即Date
        y, m, d = map(int, str_date.split('-'))
        return cls(y, m, d)

    @staticmethod
    def is_date_valid(str_date):
        y, m, d = map(int, str_date.split('-'))
        return 1 <= d <= 31 and 1 <= m <= 12 and y < 4000

if __name__ == '__main__':
    d1 = Date(2018, 8, 22)
    if Date.is_date_valid('2018-02-22'):
        d2 = Date.create_date('2018-02-22')
        print(d2)
