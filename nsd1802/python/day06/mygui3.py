import tkinter
from functools import partial

def hello(word):
    def welcome():
        lb.config(text="Hello %s!" % word)
    return welcome  # hello函数的返回值还是函数

root = tkinter.Tk()
lb = tkinter.Label(text="Hello world!", font="Times 26")
MyBtn = partial(tkinter.Button, root, fg='white', bg='blue')
b1 = MyBtn(text='Button 1', command=hello('China'))
b2 = MyBtn(text='Button 2', command=hello('tedu'))
b3 = MyBtn(text='quit', command=root.quit)
lb.pack()
b1.pack()
b2.pack()
b3.pack()
root.mainloop()

