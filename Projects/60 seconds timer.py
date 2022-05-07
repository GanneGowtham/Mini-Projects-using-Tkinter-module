from tkinter import *

root=Tk()

global time
time=60

def countdown():
    global time 

    if time>0:
        time_label.config(text="Time Left: "+str(time))
        time-=1
        time_label.after(1000, countdown)
    

time_label=Label(root, text="Time Left: ", font=('helectiva', 20, 'bold'))
time_label.pack()

start_button=Button(root, text="Start", command=countdown)
start_button.pack()

root.mainloop()
