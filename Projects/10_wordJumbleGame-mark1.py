from tkinter import *
from random import choice, shuffle
from tkinter import messagebox

root=Tk()
root.geometry('600x400')


jumble_word=Label(root, text='Country Guessing Game', font=('arial', 24))
jumble_word.pack()

global score
score=0

global timeleft
timeleft=60

score_label=Label(root, text='Click enter Button to start', font=('arial', 12))
score_label.pack(pady=10)

time_label=Label(root, text="Time Left: "+str(timeleft), font=('arial', 12))
time_label.pack(pady=5)

ans_entry=Entry(root, borderwidth=3, font=('arial', 20))
ans_entry.pack()

def start_game(event):
    if timeleft==60:
        countdown()
        shuffler()
        score_label.config(text="Score: 0")
    else:
        check()

def countdown():
    global timeleft

    if timeleft==0:
        messagebox.showinfo("Time Over", "Time over & your score is: "+str(score))
    if timeleft>0:
        timeleft-=1
        time_label.config(text="Time Left: "+str(timeleft))
        time_label.after(1000, countdown)


def shuffler():
    ans_entry.delete(0,END)
    countries=['Afghanistan','Albania','Algeria','Andorra','Angola','Antigua','Argentina','Armenia','Australia','Austria','Azerbaijan',
               'Bahamas','Bahrain','Bangladesh','Barbados','Belarus','Belgium','Belize','Benin','Bhutan','Bolivia','Bosnia', 'Botswana','Brazil','Brunei','Bulgaria','Burkina', 'Burundi',
              ]
    global word_ans
    
    word=choice(countries)
    word_ans=word
    word=list(word)
    shuffle(word) #shuffling all letters in a list using shuffle keyword.

    shuffled=''.join(word)
    jumble_word.config(text=shuffled)

def check():
    global word_ans
    global score
    global timeleft

    if timeleft>0:
        if ans_entry.get().lower()==word_ans.lower():
            score+=1
            ans_label.config(text="Correct", bg="lime")
        else:
            score-=1
            ans_label.config(text=word_ans+' is the answer!', bg="tomato")
        score_label.config(text="Score: "+str(score))
        shuffler()



start_button=Button(root, text="Start", font=('arial', 16), command=check, relief='ridge')
start_button.pack(pady=10)

ans_label=Label(root, text='', font=('lucida',16))
ans_label.pack(pady=10)


root.bind('<Return>', start_game)
root.mainloop()