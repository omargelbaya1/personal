from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank=[]
for i in question_data:
    t=i["text"]
    a=i["answer"]
    new_q=Question(t,a)
    question_bank.append(new_q)

quiz = QuizBrain(question_bank)


while quiz.still_has_question():
    quiz.ask_user()


