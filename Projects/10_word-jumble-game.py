from tkinter import *
from random import choice, shuffle

root=Tk()
root.geometry('600x400')


jumble_word=Label(root, text='', font=('arial', 20))
jumble_word.pack()

score_label=Label(root, text='', font=('arial', 14))
score_label.pack(pady=10)

global score
score=0

global time
time=60

ans_entry=Entry(root, borderwidth=3, font=('arial', 20))
ans_entry.pack()



def check():
    global word_ans
    global score

    if ans_entry.get().lower()==word_ans.lower():
        score+=1
        ans_label.config(text="Correct", bg="lime")
    else:
        score-=1
        ans_label.config(text=word_ans+' is the answer!', bg="tomato")
    score_label.config(text="Score: "+str(score))

    ans_entry.delete(0,END)
    return shuffler()
    

def shuffler():
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



start_button=Button(root, text="Start",font=('arial', 16),relief='ridge', command=shuffler)
start_button.pack(pady=10)

check_button=Button(root, text="check", font=('arial', 16), command=check, relief='ridge')
check_button.pack(pady=10)

ans_label=Label(root, text='', font=('lucida',16))
ans_label.pack(pady=10)

root.mainloop()