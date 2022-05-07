from tkinter import *

window = Tk()
window.geometry("250x200")

tally_font=("lucida", 16, "bold")

e=Entry(window, borderwidth=3, font=tally_font)
e.insert(0, "click start")
e.grid(row=0, column=0, columnspan=3)

def start_button():
    e.delete(0, END)
    e.insert(0, 0)
    global count
    
def reset_button():
    e.delete(0, END)
    e.insert(0, "click start")

def plus_button():
    # global count
    # c=e.get()
    # e.delete(0, END)
    # count = 1+int(c)
    # e.insert(0, count)
    c=e.get()
    e.delete(0, END)
    c=int(c)+1
    e.insert(0, c)

def minus_button():
    # c=e.get()
    # e.delete(0, END)
    # count = int(c) - 1
    # e.insert(0, count)
    c=e.get()
    e.delete(0, END)
    c=int(c)-1
    e.insert(0, c)

start_button=Button(window, text="START", bg="lime",relief='ridge', font=tally_font, command = start_button)
start_button.grid(row=1, column=0)

reset_button=Button(window, text="RESET", bg="tomato",relief='ridge', font=tally_font, command = reset_button)
reset_button.grid(row=1, column=2)

plus_button=Button(window, text="+", font=tally_font,relief='ridge', padx=2, pady=4, command = plus_button)
plus_button.grid(row=1, column=1, sticky='nsew')

minus_button=Button(window, text="-", font=tally_font,relief='ridge', padx=5, pady=5, command = minus_button)
minus_button.grid(row=2, column=1, sticky='nsew')

window.mainloop()