# 有双下划线的方法，一般都是python自带的方法，被称作magic
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return '《%s》' % self.title

    def __call__(self):
        print('《%s》 is written by %s' % (self.title, self.author))

if __name__ == '__main__':
    core_py = Book('Core Python', 'Wesley')  # 调用__init__
    print(core_py)  # 调用__str__
    core_py()  # 调用__call__
