from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json



#---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
    password_input.delete(0,END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)
    password_list = []
    password_list+=[random.choice(letters) for letter in range(nr_letters)]
    password_list+=[random.choice(symbols) for symbol in range(nr_symbols)]
    password_list+=[random.choice(numbers) for number in range(nr_numbers)]
    random.shuffle(password_list)
    password="".join(password_list)
    password_input.insert(0,password)
    pyperclip.copy(password)

def search_website():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()
    try:
        with open("data.json","r") as f:
            data = json.load(f)
    except FileNotFoundError:
        messagebox.showinfo(title="Data file not found", message="File not present, please add a entry first!")
    else:
        if website in data:
            new_data=data[website]
            email=new_data["email"]
            password = new_data["password"]
            print(email,password)
            messagebox.showinfo(title="Website Information", message=f"Email: {email} \n Password: {password}")
        else:
            messagebox.showinfo(title="Not Present", message="Website not present")




# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password_to_file():
    website=website_input.get()
    email=email_input.get()
    password=password_input.get()
    new_data={website:
              {
                  "email":email,
                "password":password}
              }

    if len(website_input.get())==0 or len(password_input.get())==0:
        messagebox.showinfo(title="Issue with entries" ,message="Please don't leave any fields empty")
        return
    else:
        try:
            with open("data.json", "r") as f:
                #Reading the old date
                data=json.load(f)
        except FileNotFoundError:
            with open("data.json","w") as f:
                json.dump(new_data, f, indent=4)
        else:
            # updating data variable
            data.update(new_data)
            with open("data.json", "w") as f:
                #Loading in new data
                json.dump(data,f,indent=4)
        finally:
                website_input.delete(0,END)
                password_input.delete(0,END)



# ---------------------------- UI SETUP ------------------------------- #

#window
window =Tk()
window.title("Password Manager")
window.config(padx=50,pady=50 ,bg="white")

#canvas
canvas = Canvas(width=200,height=200,highlightthickness=0,bg="white")
logo=PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo)
canvas.grid(column=1,row=0)

#labels
website_label=Label(text="Website:")
website_label.grid(column=0,row=1)
email_label=Label(text="Email/Username:")
email_label.grid(column=0,row=2)
password_label=Label(text="Password:")
password_label.grid(column=0,row=3)


#inputs
website_input = Entry(width=18,highlightthickness=0)
website_input.grid(column=1,row=1,columnspan=1)
website_input.focus()
email_input = Entry(width=35,highlightthickness=0)
email_input.grid(column=1,row=2,columnspan=2)
email_input.insert(0,"omargelbaya1@gmail.com")
password_input = Entry(width=18,highlightthickness=0)
password_input.grid(column=1,row=3)


#buttons
password_button = Button(text="Generate password",highlightbackground="white",command=generate_password)
password_button.grid(column=2,row=3)
add_button = Button(text="Add",width=36,highlightbackground="white",command=save_password_to_file)
add_button.grid(column=1,row=4,columnspan=2)
search_button = Button(text="Search",highlightbackground="white",command=search_website)
search_button.grid(column=2,row=1)






window.mainloop()