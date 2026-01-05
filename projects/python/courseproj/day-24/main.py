# with open("my_file.txt") as file:
#     contents=file.read()
#     print(contents)



with open("new_file.txt", mode='a') as file:
    for i in range(1, 100):
        file.write("\nomar")
