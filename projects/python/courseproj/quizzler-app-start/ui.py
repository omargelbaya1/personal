from email.contentmanager import get_non_text_content
from tkinter import *
from quiz_brain import QuizBrain

from pandas.io.sas.sas_constants import page_bit_offset_x64

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz_brain:QuizBrain):
        self.quiz=quiz_brain
        self.window= Tk()
        self.window.title("Quizzler")
        self.window.config(background=THEME_COLOR,padx=20,pady=20)

        #canvas
        self.canvas=Canvas(width=300,height=250,bg="white")
        self.question_text=self.canvas.create_text(
            150,
            125,
            width=280,
            text="Question here",
            fill=THEME_COLOR,
            font=("ariel",20,"italic")
        )
        self.canvas.grid(column=0,row=1,columnspan=2)


        #labels
        self.score_label= Label(highlightcolor="white", text="Score: 0",pady=20,bg=THEME_COLOR)
        self.score_label.grid(column=1,row=0)

        #buttons
        self.correct_img = PhotoImage(file="images/true.png")
        self.wrong_img = PhotoImage(file="images/false.png")
        self.correct = Button(image=self.correct_img,pady=20,padx=20,highlightthickness=0,command=self.correct_answer)
        self.correct.grid(column=0, row=3)
        self.wrong = Button(image=self.wrong_img,pady=20,padx=20,highlightthickness=0,command=self.wrong_answer)
        self.wrong.grid(column=1, row=3)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text=self.quiz.next_question()
            self.canvas.itemconfig(self.question_text,text=q_text)
        else:
            self.canvas.itemconfig(self.question_text,text="youve reached end of quiz buddy")
            self.wrong.config(state="disabled")
            self.correct.config(state="disabled")

    def correct_answer(self):
        is_right=self.quiz.check_answer("true")
        self.give_feedback(is_right)


    def wrong_answer(self):
        is_right=self.quiz.check_answer("false")
        self.give_feedback(is_right)

    def give_feedback(self,is_right):
        if is_right:
            self.canvas.config(bg="green")
            self.window.after(1000,self.get_next_question)
        else:
            self.canvas.config(bg="red")
            self.window.after(1000,self.get_next_question)


