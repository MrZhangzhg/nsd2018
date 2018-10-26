class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return "《%s》" % self.title

    def __call__(self):
        print('《%s》 is written by %s' % (self.title, self.author))

if __name__ == '__main__':
    core_py = Book(title='Core Python', author='Wesley')
    print(core_py)
    core_py()



