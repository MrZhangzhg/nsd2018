import tkinter
from functools import partial

# def welcome():
#     lb.config(text="Hello China")
#
# def hello():
#     lb.config(text="Hello Tedu")

def say_hi(word):
    def greet():
        lb.config(text="Hello %s!" % word)
    return greet

root = tkinter.Tk()  # 相当于创建窗口、标签、按钮
lb = tkinter.Label(root, text='Hello World!', font="25")
b1 = tkinter.Button(root, bg='blue', fg='white', text="Button 1")
MyButton = partial(tkinter.Button, root, bg='blue', fg='white')
b2 = MyButton(text="Button 2", command=say_hi("China"))
b3 = MyButton(text="Button 3", command=say_hi("TEDU"))
b4 = MyButton(text="QUIT", command=root.quit)
for item in [lb, b1, b2, b3, b4]:  # 将标签、按钮安装到窗口
    item.pack()
root.mainloop()   # 运行窗口程序
