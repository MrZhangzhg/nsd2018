import tkinter
from functools import partial
#
# def hello():
#     lb.config(text="Hello China!")
#
# def greet():
#     lb.config(text="Hello Tedu!")

def welcome(word):
    def say_hi():
        lb.config(text='Hello %s!' % word)
    return say_hi

root = tkinter.Tk()
lb = tkinter.Label(root, text='Hello World!',  font=("Arial, 20"))
MyButton = partial(tkinter.Button, root, fg='white', bg='blue')
# b1 = MyButton(text='Button 1', command=hello)
# b2 = MyButton(text='Button 2', command=greet)
b1 = MyButton(text='Button 1', command=welcome('China'))
b2 = MyButton(text='Button 2', command=welcome('Tedu'))
b3 = MyButton(text='QUIT', command=root.quit)
for item in [lb, b1, b2, b3]:
    item.pack()
root.mainloop()
