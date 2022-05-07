from tkinter import *

screen = Tk()

def ring():
    screen.bell()

bell_button = Button(screen, text='Ring', font='helectiva 10 bold', command=ring, relief='ridge')
bell_button.pack(pady=20,ipady=20, ipadx=10)

screen.mainloop()