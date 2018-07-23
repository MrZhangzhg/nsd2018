class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return '《%s》' % self.title

    def __call__(self):
        print('《%s》is written by %s' % (self.title, self.author))

if __name__ == '__main__':
    py_book = Book('Core Python', 'Wysley', 800)
    print(py_book)  # 调用__str__
    py_book()  # 调用__call__
