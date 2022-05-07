from tkinter import*

tk = Tk()
tk.geometry('750x300') #window size.

mylabel1 = Label(tk, text="Hello World", font='arial 40')
mylabel2 = Label(tk, text="My name is Gowtham", font='lucida 50')

mylabel1.pack()
mylabel2.pack()

tk.mainloop()