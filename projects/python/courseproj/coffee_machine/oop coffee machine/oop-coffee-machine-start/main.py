from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


my_menu=Menu()
my_cof=CoffeeMaker()
my_money=MoneyMachine()

def price_of_drinks(drink):
    if drink =="latte":
        return 2.5
    elif drink =="espresso":
        return 1.5
    elif drink =="cappuccino":
        return 3.5

coffee_machine_on=True
while coffee_machine_on:
    resources=True
    while resources:
        my_menu.name=input("What would you like? (espresso/latte/cappuccino/):")

        if my_menu.name=="off":
            exit()
        elif my_menu.name=="report":
            my_cof.report()
        else:
            drink= my_menu.find_drink(my_menu.name)
            is_sufficient=my_cof.is_resource_sufficient(drink)
            if is_sufficient and my_money.make_payment(drink.cost):
                my_cof.make_coffee(drink)
                my_cof.report()
                my_money.report()
            else:
                resources=False







print(my_menu.name)



