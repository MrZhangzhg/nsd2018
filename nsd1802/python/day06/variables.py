x = 10

def foo():
    print(x)

foo()

def bar():
    x = 20
    print(x)

bar()  # x -> 20
print(x)  # x -> 10

def aaa():
    global x
    x = 100
    print(x)  # x -> 100

print(x)  # x -> 100
