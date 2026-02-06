# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }
#
# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass
#
# import pandas
# student_data_frame = pandas.DataFrame(student_dict)
#
# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}
import pandas

nato_df=pandas.read_csv("nato_phonetic_alphabet.csv")
new_dict={row.letter:row.code for (index, row) in nato_df.iterrows()}






def trying_stuff():
    name = input("Enter a name").upper()
    try:
        another_list=[new_dict[letter] for letter in name ]
    except KeyError:
        print("Please type in something useful bro")
        trying_stuff()
    else:
        print(another_list)

trying_stuff()