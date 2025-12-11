# from turtle import Turtle, Screen
from prettytable import PrettyTable

# timmy = Turtle()
# my_screen= Screen()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("coral")
# timmy.forward(100)
# print(my_screen.canvheight)
# my_screen.exitonclick()

table=PrettyTable()

table.add_column("Pokemon Name",["Pikachu","Squirtle","Charmander"])
table.add_column("Type",["Electric","Water","Fire"])
table.align='l'
print(table)