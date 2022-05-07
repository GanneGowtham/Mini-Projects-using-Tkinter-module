from tkinter import *

tk =Tk()

mylabel1 = Label(tk, text="Hello world")
mylabel2 = Label(tk, text="My name is GanneGowtham")
mylabel3 = Label(tk, text="This is done using Tkinter", fg='skyblue')

mylabel1.grid(row=0, column=0)
mylabel2.grid(row=1, column=0)
mylabel3.grid(row=2, column=0)

tk.mainloop()