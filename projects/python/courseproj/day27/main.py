from tkinter import *


window = Tk()

window.title("My First program")
window.minsize(width=500,height=300)

#Label

my_label =Label(text="I am a label",font=("Arial",24,"bold"))
my_label.grid(column=1,row=0)

my_label["text"] = "New Text"
my_label.config(text="New Text")

#Button
def button_clicked():
    my_label["text"] = entry_example()

button = Button(text="Click Me", command=button_clicked)
button.grid(column=4,row=4)

button2 = Button(text="new button")
button2.grid(column=3,row=0)


#Entry

input = Entry(width=10)
input.grid(column=2,row=2)

def entry_example():
    return input.get()




window.mainloop()
