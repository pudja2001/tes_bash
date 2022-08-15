from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_makers = CoffeeMaker()
menu = Menu()
machine = MoneyMachine()


commands_ = str(input("What would you like to do? (drink/report/off): "))
commands_ = commands_.lower()
while True:
    if commands_ == 'drink':
        options = menu.get_items()
        print("\n")
        choice = input("What would you like? ({options}): ")
        if choice in ['espresso', 'latte', 'cappucino']:
            drink = menu.find_drink(choice)
            if coffee_makers.is_resource_sufficient(drink):
                print("Name :", drink.name)
                print("Cost :", drink.cost)
                print("\n")
                if machine.make_payment(drink.cost):
                    print(f"{drink.name} is being made")
                    coffee_makers.make_coffee(drink)
                    print("Finished")
                else:
                    print("Sorry that's not enough money. Money refunded")
                
            else:
                print("Sorry there is not enough water.")

        else:
            print("There's no such drinks.")
    elif commands_ == 'report':
        print("\n")
        print('Current Money :')
        machine.report()
        print('Current Resources:')
        coffee_makers.report()
    elif commands_ == 'off':
        break
    print("\n")
    commands_ = str(input("What would you like to do? (drink/report/off): "))
    commands_ = commands_.lower()



# print("Pudja".lower())