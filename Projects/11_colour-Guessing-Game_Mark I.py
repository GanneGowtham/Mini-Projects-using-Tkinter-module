from tkinter import *
from random import choice

root = Tk()

font_style1=('helectiva', 20)
font_style2=('lucida', 14)

def validate_color():
    global colour
    if answer_box.get()==colour:
        answer_label.config(text="Correct")
    else:
        answer_label.config(text="Incorrect")
    answer_label.after(400, lambda: answer_label.config(text=''))
    answer_box.delete(0, END)
    generate()

def generate():
    global colour

    colours=['red', 'blue', 'green', 'yellow', 'orange', 'pink', 'black', 'grey', 'violet', 'indigo']
    words=['red', 'blue', 'green', 'yellow', 'orange', 'pink', 'black', 'grey', 'violet', 'indigo']
    
    colour=choice(colours)
    word=choice(words)

    color_display.config(text=word, fg=colour)


color_display=Label(root, text="Colour Guessing Game", font=font_style1)
color_display.grid(row=0, column=0, pady=10, columnspan=2)

answer_box=Entry(root, text="", font=font_style2, borderwidth=3)
answer_box.grid(row=2, column=0, ipadx=10, ipady=5, pady=10, columnspan=2)

generate_button=Button(root, text="Generate", font=font_style2, borderwidth=3, command=generate)
generate_button.grid(row=3, column=0, sticky='nsew')

check_button=Button(root, text="check", font=font_style2, borderwidth=3, command=validate_color)
check_button.grid(row=3, column=1, sticky='nsew')

answer_label=Label(root, text='', font=font_style2)
answer_label.grid(row=4, column=0, pady=10, columnspan=2)

root.mainloop()