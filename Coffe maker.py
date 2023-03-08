import water

from menu import MENU, resources
import random


def resource_check(drink):
    if resources['water'] - MENU[drink]['ingredients']['water'] > 0:
        if resources['coffee'] - MENU[drink]['ingredients']['coffee'] > 0:
            if resources['milk'] - MENU[drink]['ingredients']['milk'] > 0:
                return True
            else:
                print("Not enough milk.")
        else:
            print("Not enough coffee.")
    else:
        print("Not enough water.")



def funds(payment):
    if payment - MENU[drink]['cost']>=0:
        change=payment - MENU[drink]['cost']
        print(f"Your chnage is {change}")
        return True
    else:
        print("Insufficient funds. Here's a refund.")



print(resources)
drink = input("What would you like to drink?: ")
resources1=resource_check(drink)
drink_cost=(MENU[drink]['cost'])


if resources1 == True:
    print(f"Your drink costs {drink_cost}")
    quarters = float(input("How many Quarters?: ")) * 0.25
    nickels = float(input("How many Nickles?: ")) * .05
    dimes = float(input("How many Dimes?: ")) * .10
    pennies = float(input("How many Pennies?: ")) * .01
    payment = quarters + nickels + dimes + pennies
    if funds(payment) == True:
        print(f"Now making your {drink}")
        resources['water'] -= MENU[drink]['ingredients']['water']
        resources['coffee'] -= MENU[drink]['ingredients']['coffee']
        resources['milk'] -= MENU[drink]['ingredients']['milk']
        print(resources)





