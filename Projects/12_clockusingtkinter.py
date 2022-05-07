from tkinter import*
from time import *

root = Tk()
root.title("Clock")

time_label1 = Label(root, text='', font='arial 20 bold')
time_label1.config(text=strftime('%a, %d %b %Y'))
time_label1.pack()

time_label2=Label(root, font=('lucida',20, 'bold'), text='')
time_label2.pack()

time_label3 = Label(root, text='', font=('calibri 20 bold'))
time_label3.config(text=strftime('Time Zone: %z'))
time_label3.pack()

def time():
    present_time=strftime('%H:%M:%S %Z')
    # %H(Hours), %M(Minutes), %S(Seconds), %x(month/date/year), %Z(IST)
    # using '%H %M %S' instead '%X' can be used, it also shows hours, minutes, seconds
    time_label2.config(text=present_time)
    time_label2.after(1000,time)
time()

root.mainloop()