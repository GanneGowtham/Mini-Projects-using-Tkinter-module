from tkinter import *
from random import choice

root = Tk()

font_style1=('helectiva', 20)
font_style2=('lucida', 14)

global time
time=60

global score
score=0

def start_game(event):
    global time

    if time==60:
        countdown()
        generate()
        score_label.config(text='Score: 0')
    else:
        validate_color()

def countdown():
    global time

    if time>0:
        time-=1
        timeleft.config(text="Time Left: "+str(time))
        timeleft.after(1000, countdown)

def validate_color():
    global colour
    global score
    if time>0:
        if answer_box.get()==colour:
            answer_label.config(text="Correct")
            score+=1
        else:
            answer_label.config(text="Incorrect")
            score-=1
        
        score_label.config(text='Score: '+str(score))

        answer_label.after(400, lambda: answer_label.config(text=''))
        answer_box.delete(0, END)
        generate()

def generate():
    global colour

    colours=['red', 'blue', 'green', 'yellow', 'orange', 'pink', 'black', 'grey', 'violet', 'indigo', 'brown', 'white']
    words=['red', 'blue', 'green', 'yellow', 'orange', 'pink', 'black', 'grey', 'violet', 'indigo', 'brown', 'white']
    
    colour=choice(colours)
    word=choice(words)

    color_display.config(text=word, fg=colour)


color_display=Label(root, text="Colour Guessing Game", font=font_style1)
color_display.grid(row=0, column=0, pady=10, columnspan=2)

score_label=Label(root, text="Click on  enter to start the game", font=font_style2)
score_label.grid(row=1, column=0)

timeleft=Label(root, text="Timeleft: 60", font=font_style2)
timeleft.grid(row=1, column=1)

answer_box=Entry(root, text="", font=font_style2, borderwidth=3)
answer_box.grid(row=2, column=0, ipadx=10, ipady=5, pady=10, columnspan=2)

answer_label=Label(root, text='', font=font_style1)
answer_label.grid(row=4, column=0, columnspan=2)

root.bind('<Return>', start_game)
root.mainloop()
