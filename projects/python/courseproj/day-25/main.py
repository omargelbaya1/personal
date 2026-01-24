

# with open("weather_data.csv", mode='r') as file:
#     data= file.readlines()
#     print(data)


# import csv
#
#
# with open("weather_data.csv") as file:
#     data = csv.reader(file)
#     temperatures=[]
#     for row in data:
#         if row[1]!="temp":
#             temperatures.append(int(row[1]))
#
#     print(temperatures)

# data =  pandas.read_csv("weather_data.csv")
# data_dict=data.to_dict()
# temp_list=data["temp"].to_list()
#
#
# print(data["temp"].mean())
# print(data["temp"].max())
#
#
#
# monday = data[data.day=="Monday"]
# celsius=monday.temp
# farhenheit=((9/5)* celsius) +32
# print(farhenheit)

# data_dict={
#     "students": ["Amy","James","Angela"],
#     "score": [76,56,65]
# }
#
# df = pandas.DataFrame(data_dict)
# print(df)
# df.to_csv("new_data.csv")


import pandas

df =  pandas.read_csv("squirrel.csv")

cinnamon = df[df["Primary Fur Color"]=="Cinnamon"]
gray = df[df["Primary Fur Color"]=="Gray"]
black = df[df["Primary Fur Color"]=="Black"]

print(cinnamon,gray,black)



df_dict={
    "Fur Color":["grey","red","black"],
    "count":[len(gray),len(cinnamon),len(black)]
}

dff=pandas.DataFrame(df_dict)
dff.to_csv("squirrel_count.csv")
