from tkinter import *

root=Tk()

l=Label(root, text="Enter your name in below entry box and click button")
l.pack()

e=Entry(root, borderwidth=5)
#e.insert(0,"Enter your name:")
e.pack()

def click():
    s="Hello "+e.get()
    mylabel=Label(root, text=s)
    mylabel.pack()
    e.delete(0, END)

b=Button(root, text="click here", bg="white", command=click)
b.pack()
root.mainloop()