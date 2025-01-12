from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
import time

def skip(seconds):
    time.sleep(seconds)
    print('\n' * 50)

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

while True:
    #skip(0)
    choice = input(f'What would you like? ({menu.get_items()}): ')
    
    if choice == 'off':
        print('Turning it off...')
        skip(2)
        break

    elif choice == 'report':
        coffee_maker.report()
        money_machine.report()
        skip(3)
    
    else:
        drink = menu.find_drink(choice)
        if drink != None and coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
            skip(4)
        else:
            skip(2)

