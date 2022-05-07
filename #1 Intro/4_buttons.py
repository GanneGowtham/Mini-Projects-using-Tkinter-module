from tkinter import *

root = Tk()
root.geometry("400x300")

def mybutton():
    mylabel=Label(root, text="submitted")
    mylabel.pack()

label1 = Label(root, text='In the above button fill=X is used!')
button1 = Button(root, text="CLICK HERE", fg="green", bg="white", font="arial 10 bold", padx=10)  
button2 = Button(root, text="click here", state=DISABLED) #state=DISABLED makes the button disable.
button3 = Button(root, text="submit",fg="white", bg="black", font='lucida 10 bold', command=mybutton)

text1=Label(root, text="Types of Buttons as follows", font="arial 18 bold")
button_raised=Button(root, text="Raised Button", relief="raised") 
button_sunken=Button(root, text="Sunken Button", relief="sunken")
button_flat=Button(root, text="Flat Button", relief="flat") # relief is used for getting shape of button.
button_ridge=Button(root, text="Ridge Button", relief="ridge")
button_solid=Button(root, text="Solid Button", relief="solid")
button_groove=Button(root, text="Groove Button", relief="groove")

'''
fg-> foreground colour, bg-> background color 
padx=width inbetween internal area, pady=height between the internal area.
ipad is used to increase the height or width between two external states/labels.
state-> describes the state of button.

'''

button1.pack(fill=X)  # fill=X is used for the buttons to fill the screen horizontally. 
label1.pack(ipady=5)
button2.pack()
button3.pack()

text1.pack()
button_raised.pack()
button_sunken.pack()
button_flat.pack()
button_ridge.pack()
button_solid.pack()
button_groove.pack()


root.mainloop()