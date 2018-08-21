import tkinter
from functools import partial

# def hello():
#     lb1.config(text='Hello China')
#
# def welcome():
#     lb1.config(text='Hello Tedu')

def say_hi(word):
    def greet():
        lb1.config(text='Hello %s' % word)
    return greet

root = tkinter.Tk()
lb1 = tkinter.Label(root, text='Hello World', font='Arial 25')
MyButton = partial(tkinter.Button, root, bg='blue', fg='white')
b1 = MyButton(text='Button 1', command=say_hi('China'))
b2 = MyButton(text='Button 2', command=say_hi('Tedu'))
b3 = MyButton(text='Button 3', command=root.quit)
lb1.pack()
b1.pack()
b2.pack()
b3.pack()
root.mainloop()