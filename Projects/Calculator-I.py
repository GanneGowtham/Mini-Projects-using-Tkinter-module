from tkinter import *

root=Tk()
root.title("Calculator")

e=Entry(root, borderwidth=3, width=20, font="lucida 20 bold")
e.grid(row=0, column=0, pady=10, columnspan=5)

f_style = ("Arial", 16, "bold")

def button_click(num):
    current=e.get()
    e.delete(0,END)
    e.insert(0,str(current)+str(num))

def button_clear():
    e.delete(0,END)

def button_add():
    global f_num
    global math
    math="add"
    f_num=e.get()
    e.delete(0,END)

def button_substract():
    global f_num
    global math
    math ="substract"
    f_num=e.get()
    e.delete(0, END)

def button_multiply():
    global math
    global f_num
    math="multiply"
    f_num=e.get()
    e.delete(0, END)

def button_division():
    global math
    global f_num
    math="division"
    f_num=e.get()
    e.delete(0,END)

def button_equal():
    second_num=e.get()
    e.delete(0,END)
    if math=="add":
        e.insert(0, int(f_num) + int(second_num))
    elif math=="substract":
        e.insert(0, int(f_num) - int(second_num))
    elif math=="multiply":
        e.insert(0, int(f_num) * int(second_num))
    elif math=="division":
        if int(second_num)==0:
            e.insert(0, "Cannot divide by zero")
        else:
            e.insert(0, int(f_num)/int(second_num))

#Define Buttons
button_1=Button(root, text="1", width=4, height=2, bg="white", font = f_style, relief='ridge', command=lambda: button_click(1))
button_2=Button(root, text="2", width=4, height=2, bg="white", font = f_style, relief='ridge', command=lambda: button_click(2))
button_3=Button(root, text="3", width=4, height=2, bg="white", font = f_style, relief='ridge', command=lambda: button_click(3))
button_4=Button(root, text="4", width=4, height=2, bg="white", font = f_style, relief='ridge', command=lambda: button_click(4))
button_5=Button(root, text="5", width=4, height=2, bg="white", font = f_style, relief='ridge', command=lambda: button_click(5))
button_6=Button(root, text="6", width=4, height=2, bg="white", font = f_style, relief='ridge', command=lambda: button_click(6))
button_7=Button(root, text="7", width=4, height=2, bg="white", font = f_style, relief='ridge', command=lambda: button_click(7))
button_8=Button(root, text="8", width=4, height=2, bg="white", font = f_style, relief='ridge', command=lambda: button_click(8))
button_9=Button(root, text="9", width=4, height=2, bg="white", font = f_style, relief='ridge', command=lambda: button_click(9))
button_0=Button(root, text="0", width=4, height=2, bg="white", font = f_style, relief='ridge', command=lambda: button_click(0))

button_add=Button(root, text="+", width=4, height=2, fg="#009698", relief='ridge', font = f_style, command= button_add)
button_equal=Button(root, text="=", width=4, height=2, font = f_style, bg="orange", relief='ridge', command= button_equal)
button_clear=Button(root, text="clear", width=4, height=2, font = f_style, relief='ridge', command= button_clear)
button_substract=Button(root, text="-", width=4, height=2, fg="#32cd32", font = f_style, relief='ridge', command= button_substract)
button_multiply=Button(root, text="x", width=4, height=2, fg="tomato", font = f_style, relief='ridge', command= button_multiply)
button_division=Button(root, text="%", width=4, height=2, fg="#fcc200", font = f_style, relief='ridge', command= button_division)
#put buttons on screen
button_9.grid(row=1, column=0, sticky='nsew')
button_8.grid(row=1, column=1, sticky='nsew')
button_7.grid(row=1, column=2, sticky='nsew')

button_6.grid(row=2, column=0, sticky='nsew')
button_5.grid(row=2, column=1, sticky='nsew')
button_4.grid(row=2, column=2, sticky='nsew')

button_3.grid(row=3, column=0, sticky='nsew')
button_2.grid(row=3, column=1, sticky='nsew')
button_1.grid(row=3, column=2, sticky='nsew')
button_0.grid(row=4, column=1, sticky='nsew')

button_add.grid(row=2, column=4, sticky='nsew')
button_equal.grid(row=5,column=0, columnspan=3, sticky='nsew')
button_clear.grid(row=5, column=4, sticky='nsew')

button_substract.grid(row=3, column=4, sticky='nsew')
button_multiply.grid(row=1, column=4, sticky='nsew')
button_division.grid(row=4, column=4, sticky='nsew')

root.mainloop()
