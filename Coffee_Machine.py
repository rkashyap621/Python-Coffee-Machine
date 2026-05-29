from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
       
my_menu=Menu()
my_coffee_maker=CoffeeMaker()
my_money_machine=MoneyMachine()

machine_state=True

while machine_state:
    drink_choice= input("What do you want to drink?("+my_menu.get_items()+"): ")
    if drink_choice=="off":
        machine_state=False
    elif drink_choice=="report":
        my_coffee_maker.report()
        my_money_machine.report()
    else:
        drink_item=my_menu.find_drink(drink_choice)
        if my_coffee_maker.is_resource_sufficient(drink_item) and my_money_machine.make_payment(drink_item.cost):
                my_coffee_maker.make_coffee(drink_item)
