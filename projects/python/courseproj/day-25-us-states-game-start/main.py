import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S States Game")
image= "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

df = pandas.read_csv("50_states.csv")

guessed_states=[]
all_states= df.state.to_list()


while len(guessed_states) < 50:
    answer_state= screen.textinput(title=f"{len(guessed_states)}/50 Guess the state", prompt="Whats another state").title()
    if answer_state=="Exit":
        df=pandas.DataFrame(all_states)
        df.to_csv("missed_states.csv")
        break
    if answer_state in all_states:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data=df[df.state==answer_state]
        t.goto(state_data.x.item(),state_data.y.item())
        t.write(answer_state)
        guessed_states.append(answer_state)
        all_states.remove(state_data.state.item())
        print(all_states)

