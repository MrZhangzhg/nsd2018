class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    @classmethod
    def create_date(cls, str_date):
        y, m, d = map(int, str_date.split('-'))
        instance = cls(y, m, d)
        return instance

    @staticmethod
    def is_date_valid(str_date):
        y, m, d = map(int, str_date.split('-'))
        return y < 4000 and 0 < m < 13 and 0 < d < 32

if __name__ == '__main__':
    d1 = Date(2018, 11, 16)
    print(d1.year)
    d2 = Date.create_date('2018-11-15')
    print(d2.month)
    print(Date.is_date_valid('2018-11-15'))
    print(Date.is_date_valid('2018-11-150'))
    # print(is_date_valid('2018-11-150'))
