#for each name in invited_names.txt
with open("/Users/omargelbaya/Documents/personal/projects/python/courseproj/Mail Merge Project Start/Input/Names/invited_names.txt", mode='r') as file:
    new_list=[]
    for i in file:
        new_list.append(i)
        print(i)

print(new_list)


with open("/Users/omargelbaya/Documents/personal/projects/python/courseproj/Mail Merge Project Start/Input/Letters/starting_letter.txt") as file2:
    content=file2.read()
    for i in new_list:
        i=i.replace("\n","")
        x=content.replace("[name]",i)
        with open(f"/Users/omargelbaya/Documents/personal/projects/python/courseproj/Mail Merge Project Start/Input/Letters/starting_{i}.txt",mode='w') as file3:
            file3.write(x)

#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp