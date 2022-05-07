from tkinter import *

root=Tk()

e = Entry(root) # creates an input box
e.insert(0,"Type here")

e1 = Entry(root, width=25, bg="tomato", borderwidth=3, font='arial 20') #an entry box with bg colour-> green, width->25, borderwidth=5
e1.insert(0, "Type here")

e2 = Entry(root, borderwidth=10) #entry box with border width 10
e2.insert(0, "Type here")

e.pack(ipady=10)
e1.pack(ipady=10)
e2.pack()

root.mainloop()