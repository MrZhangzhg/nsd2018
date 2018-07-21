import tkinter
from functools import partial

root = tkinter.Tk()
lb = tkinter.Label(text="Hello world!")
b1 = tkinter.Button(root, fg='white', bg='blue', text='Button 1')
MyBtn = partial(tkinter.Button, root, fg='white', bg='blue')
b2 = MyBtn(text='Button 2')
b3 = MyBtn(text='quit', command=root.quit)
lb.pack()
b1.pack()
b2.pack()
b3.pack()
root.mainloop()

# yum install -y tk-devel tcl-devel sqlite-devel
# ./configure --prefix=/usr/local
# make && make install
