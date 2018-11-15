class MyClass:
    def hello(self):
        print('Hello World!')

    @staticmethod    # 创建静态方法，与类没有什么关系
    def welcome():
        print('你好!')

    @classmethod     # 类方法
    def greet(cls):
        print('How are you?')

if __name__ == '__main__':
    # MyClass.hello()   错误，不能直接调用，需要通过实例调用
    MyClass.welcome()   # 静态方法可以直接调用，不需要实例
    MyClass.greet()     # 类态方法可以直接调用，不需要实例
