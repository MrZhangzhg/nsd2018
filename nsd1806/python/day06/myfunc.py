x = 10

def foo():
    print(x)

def bar():
    y = 1000
    print(y)

def foobar():
    x = 'hello'   # 局部变量将会遮盖住全局的x
    print(x)

def modify():
    global x      # 声明需要使用的x是全局变量
    x = 'ni hao'  # 将全局变量x重新赋值

# print(x)
# bar()
# print(y)   # 错误，y是bar的局部变量，只能在bar函数中使用
# foobar()
# print(x)     # 10, 函数foobar不能直接修改全局变量的值
print(x)
modify()
print(x)

