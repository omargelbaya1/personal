import os, random
import datetime as dt
import pandas as pd
##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv


# 2. Check if today matches a birthday in the birthdays.csv

current_day= dt.datetime.now().day
current_month=dt.datetime.now().month



df = pd.read_csv("birthdays.csv")

new_df = df[(df['day']== current_day) & (df['month'] == current_month)]

name=new_df["name"].item()

print(name)



# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
random_letter=random.choice(os.listdir("letter_templates/"))

y=open(f"letter_templates/{random_letter}","r")
read_letter=y.read()
print(read_letter)

new_letter=read_letter.replace("[NAME]",name)
print(new_letter)

x=(open(f"letter_templates/{random_letter}","w"))

x.write(new_letter)


# 4. Send the letter generated in step 3 to that person's email address.




