# yum install -y tk-devel tcl-devel sqlite-devel
# cd /opt        py3soft.tar.gz
# tar xzf Python3.6.1xxxx.tar.gz
# cd Python-3.6.1
# ./configure --prefix=/usr/local/
# make
# make install
import tkinter
from functools import partial

root = tkinter.Tk()
lb1 = tkinter.Label(root, text='Hello World', font='Arial 15')
MyButton = partial(tkinter.Button, root, bg='blue', fg='white')
b1 = MyButton(text='Button 1')
b2 = MyButton(text='Button 2')
b3 = MyButton(text='Button 3', command=root.quit)
lb1.pack()
b1.pack()
b2.pack()
b3.pack()
root.mainloop()
# b1 = tkinter.Button(root, bg='blue', fg='white', text='Button 1')
# b2 = tkinter.Button(root, bg='blue', fg='white', text='Button 1')
# b3 = tkinter.Button(root, bg='blue', fg='white', text='Button 1')



