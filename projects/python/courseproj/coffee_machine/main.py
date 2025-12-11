MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money":0
}

# water=300,milk=200,coffee=100

#TODO:1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
def drink_choice():
    choice=input("What would you like? (espresso/latte/cappuccino):").lower()
    return choice

#TODO:2. Turn off the Coffee Machine by entering “off” to the prompt.
def coffee_machine_off():
    if input()=="off":
        exit()

#TODO:3. Print report.
def report():
    print(f"Water:  {resources['water']}ml")
    print(f"Milk:  {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${resources['money']}")

#TODO:4. Check resources sufficient?
def resources_sufficient(resource,choice_of_drink):
    try:
        value_of_drink=(MENU[choice_of_drink]["ingredients"][resource])
    except KeyError:
        value_of_drink=0
    value_of_resources=resources[resource]
    print(value_of_resources)
    print(value_of_drink)
    if value_of_resources>value_of_drink :
        resources[resource] = value_of_resources - value_of_drink
    else:
        print(f"Sorry there is not enough {resource}")


#resources_sufficient("milk")

#TODO:5. Process coins.
def process_coins():
    quarter=0.25
    dime=0.10
    nickle=0.05
    penny=0.01
    amount_quarters=int(input("How many quarters:"))
    amount_dimes=int(input("How many dimes:"))
    amount_nickles=int(input("How many nickles:"))
    amount_pennies=int(input("How many pennies:"))
    total_amount=(quarter*amount_quarters)+(dime*amount_dimes)+(nickle*amount_nickles)+(penny*amount_pennies)
    return total_amount


#TODO:6. Check transaction successful?
def successful_transaction():
    choice_of_drink=drink_choice()
    money=MENU[choice_of_drink]["cost"]
    cost_of_drink=process_coins()
    if cost_of_drink<money:
        print("Sorry that's not enough money. Money refunded.")
    else:
        resources["money"]+=money
        change=round((cost_of_drink-money),2)
        print(f"this is your change: {change}")
        return choice_of_drink

#TODO:7. Make Coffee.
def make_coffee():
    report()
    choice_of_drink=successful_transaction()
    for i in resources:
        resources_sufficient(i,choice_of_drink)
    report()
    print(f"Thanks for using the machine, here is your drink: {choice_of_drink}")

user_wants_a_drink=True

while user_wants_a_drink:
    make_coffee()
