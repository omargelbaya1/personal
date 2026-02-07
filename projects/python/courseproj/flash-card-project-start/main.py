from tkinter import *
import pandas as pd
import random
import csv

BACKGROUND_COLOR = "#B1DDC6"



try:
    df = pd.read_csv('data/words_to_learn.csv')
except FileNotFoundError:
    df = pd.read_csv('data/arabic_to_english.csv')
else:
    to_learn=df.to_dict(orient="records")
finally:
    to_learn = df.to_dict(orient="records")

random_card={}

#------------------------------- FUNCTIONS --------------------------------------
def next_card():
    global timer
    global random_card
    window.after_cancel(timer)
    timer=window.after(10000,other_card)
    random_card= random.choice(to_learn)
    arabic = random_card["Arabic"]
    canvas.itemconfig(canvas_word_text, text=f"{arabic}",fill="black")
    canvas.itemconfig(canvas_title_text,text="Arabic",fill="black")
    canvas.itemconfig(canvas_image, image=card_front)



def other_card():
    global timer
    global random_card

    canvas.itemconfig(canvas_image, image=card_back)
    english=random_card["English"]
    canvas.itemconfig(canvas_word_text, text=f"{english}",fill="white")
    canvas.itemconfig(canvas_title_text, text="English",fill="white")

def right_button():
    next_card()
    to_learn.remove(random_card)
    words_to_learn()

def words_to_learn():
    df1=df.from_dict(to_learn)
    print(df1)
    df1.to_csv('data/words_to_learn.csv',index=False)




#window
window =Tk()
window.title("Arabic Helper!")
window.config(padx=50,pady=50 ,bg=BACKGROUND_COLOR)
timer=window.after(10000,other_card)
#canvas
canvas = Canvas(width=800,height=526)
card_front=PhotoImage(file="images/card_front.png")
card_back=PhotoImage(file="images/card_back.png")
canvas_image=canvas.create_image(400,263,image=card_front)
canvas.config(background=BACKGROUND_COLOR,highlightthickness=0)
canvas_word_text=canvas.create_text(400,263,text="",fill="black",font=("ariel",60,"bold"))
canvas_title_text=canvas.create_text(400,150,text="",fill="black",font=("ariel",40,"italic"))
canvas.grid(column=1,row=1,columnspan=2)


#buttons
my_image_right = PhotoImage(file="images/right.png")
button_right = Button(image=my_image_right, highlightthickness=0,highlightbackground=BACKGROUND_COLOR,command=right_button)
button_right.grid(column=2,row=2)
my_image_wrong = PhotoImage(file="images/wrong.png")
button_wrong = Button(image=my_image_wrong, highlightthickness=0,highlightbackground=BACKGROUND_COLOR,command=next_card)
button_wrong.grid(column=1,row=2)


next_card()

window.mainloop()