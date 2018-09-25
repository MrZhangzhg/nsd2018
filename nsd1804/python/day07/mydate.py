class Date:
    def __init__(self, year, month, date):
        self.year = year
        self.month = month
        self.date = date

    def display(self):
        print('The date is %s' % self.date)

    @classmethod  # 类方法，没有实例也可以调用
    def create_date(cls, str_date):  # cls表示类，本例中就是Date
        year, month, date = map(int, str_date.split('-'))
        return cls(year, month, date)

    @staticmethod  # 静态方法，与类方法类似，但是代码中没有使用到类
    def is_date_valid(str_date):
        year, month, date = map(int, str_date.split('-'))
        return year < 4000 and 0 < month < 13 and 0 < date < 32

if __name__ == '__main__':
    # d1 = Date(2018, 9, 25)
    # print(d1.year, d1.month, d1.date)
    print(Date.is_date_valid('4000-1-1'))
    d2 = Date.create_date('2018-10-1')
    print(d2.year, d2.month, d2.date)
    d2.display()
