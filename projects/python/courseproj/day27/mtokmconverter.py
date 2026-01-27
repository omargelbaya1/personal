from tkinter import *

#window
window = Tk()
window.title("my to km converter")
window.minsize(width=500,height=300)


#labels
miles=Label(text="Miles",font=("Arial",24,"bold"))
miles.grid(column=2,row=0)
km =Label(text="Km",font=("Arial",24,"bold"))
km.grid(column=2,row=1)
is_equal_to =Label(text="is equal to",font=("Arial",24,"bold"))
is_equal_to.grid(column=0,row=1)
input = Entry(width=10)
input.grid(column=1,row=0)

number=Label(text="0",font=("Arial",24,"bold"))
number.grid(column=1,row=1)

def button_clicked():
    number["text"] = convert(int(input.get()))

def convert(n):
    return n * 1.6

#buttons
button = Button(text="Calculate", command=button_clicked)
button.grid(column=1,row=2)





window.mainloop()
