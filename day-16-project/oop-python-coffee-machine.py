from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

machine = CoffeeMaker()
menu = Menu()
menu_item = MenuItem
money = MoneyMachine()
purchasing = True
machine_on = True
while purchasing and machine_on:
    object_name = None
    can_make = False
    while object_name is None and can_make is False and machine_on:
        selection = input(f"What type of coffee would you like? {menu.get_items()}\n").lower()
        if selection == "report":
            machine.report()
            continue
        object_name = menu.find_drink(selection)
        can_make = machine.is_resource_sufficient(object_name)
    paid = False
    while paid is False:
        print(f"Your selection will cost {object_name.cost}.")
        paid = money.make_payment(object_name.cost)
    machine.make_coffee(object_name)
    if input("Would you like another coffee? Yes/No").lower() == "no":
        purchasing = False
