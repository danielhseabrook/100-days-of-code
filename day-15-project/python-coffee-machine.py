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
}

COINS = {
    "pennies": 0.01,
    "nickels": 0.05,
    "dimes": 0.10,
    "quarters": 0.25
}


def resource_exchange(a):
    insufficient_resources_list = []
    insufficient_resources_string = ""
    if resources["water"] < MENU[a]["ingredients"]["water"]:
        insufficient_resources_list.append("water")
    elif selection != "espresso":
        if resources["milk"] < MENU[a]["ingredients"]["milk"]:
            insufficient_resources_list.append("milk")
    if resources["coffee"] < MENU[a]["ingredients"]["coffee"]:
        insufficient_resources_list.append("coffee")
    if len(insufficient_resources_list) > 0:
        insufficient_resources_string = ', '.join(insufficient_resources_list)
        return insufficient_resources_string
    resources["water"] -= MENU[a]["ingredients"]["water"]
    if selection != "espresso":
        resources["milk"] -= MENU[a]["ingredients"]["milk"]
    resources["coffee"] -= MENU[a]["ingredients"]["coffee"]
    return insufficient_resources_string


def currency_exchange(a):
    global change
    total_paid = 0
    item_price = MENU[a]["cost"]
    str_item_price = ("$" + "%.2f" % item_price)
    print(f"Your drink will cost {str_item_price}")
    while item_price - total_paid > 0:
        # How many pennies to be used
        pennies = int(input("How many pennies would you like to insert?\n") or "0")
        total_paid += pennies * COINS["pennies"]
        # If entered pennies pays off bill, leave while loop
        if item_price - total_paid <= 0:
            continue
        # How many nickels are to be used
        nickels = int(input("How many nickels would you like to insert?\n") or "0")
        total_paid += nickels * COINS["nickels"]
        # If entered nickels pay of the bill, leave while loop
        if item_price - total_paid <= 0:
            continue
        # How many dimes are to be used
        dimes = int(input("How many dimes would you like to insert?\n") or "0")
        total_paid += dimes * COINS["dimes"]
        # If entered dimes pay off the bill, leave loop
        if item_price - total_paid <= 0:
            continue
        # How many quarters are to be used
        quarters = int(input("How many quarters would you like to insert?\n") or "0")
        total_paid += quarters * COINS["quarters"]
        # Underpaid - present amount remaining and restart loop
        bill_remainder = MENU[a]['cost'] - total_paid
        str_bill_remainder = ("$" + "%.2f" % bill_remainder)
        print(f"You need to insert {str_bill_remainder} more.")
        continue
    # Check if the bill has been paid exactly, underpaid or overpaid.
    # Return $0.00 change amount if paid exactly
    if total_paid == item_price:
        resources["profit"] += item_price
        change = total_paid - item_price
        return change
    # Return change amount if overpaid
    elif total_paid > item_price:
        resources["profit"] += item_price
        change = total_paid - item_price
        return change


ordering = "yes"
machine_state = "on"
resources["profit"] = 0
acceptable_input = ['espresso', 'latte', 'cappuccino', 'report', 'off']
while machine_state == "on" and ordering == "yes":
    resources_unavailable = ""
    change = 0
    print("What sort of coffee would you like? Espresso/Latte/Cappuccino")
    selection = input("You may also enter Report or Off\n").lower()
    while selection not in acceptable_input:
        print("What sort of coffee would you like? Espresso/Latte/Cappuccino")
        selection = input("You may also enter Report or Off\n").lower()
    # Customer selected cappuccino
    if selection == "cappuccino":
        resources_unavailable = resource_exchange(selection)
        if resources_unavailable != "":
            print(f"There is an insufficient amount of {resources_unavailable} to make that drink.")
            print("Please select another.")
            continue
        else:
            currency_exchange(selection)
            if change > 0:
                change = ("$" + "%.2f" % change)
                print(f"Here is your {change} change")
    # Customer selected latte
    if selection == "latte":
        resources_unavailable = resource_exchange(selection)
        if resources_unavailable != "":
            print(f"There is an insufficient amount of {resources_unavailable} to make that drink.")
            print("Please select another.")
            continue
        else:
            currency_exchange(selection)
            if change > 0:
                change = ("$" + "%.2f" % change)
                print(f"Here is your {change} change")
    # Customer selected espresso
    if selection == "espresso":
        resources_unavailable = resource_exchange(selection)
        if resources_unavailable != "":
            print(f"There is an insufficient amount of {resources_unavailable} to make that drink.")
            print("Please select another.")
            continue
        else:
            currency_exchange(selection)
            if change > 0:
                change = ("$" + "%.2f" % change)
                print(f"Here is your {change} change and")
    # If off is entered turn machine off
    if selection == "off":
        print("The machine is turning off.")
        machine_status = "off"
        continue
    # If report is entered, print resource dict
    if selection == "report":
        print(f"Below is the current standing of the Python Coffee Machine.\n{resources}")
    # Giving customer their order
    ordering = input(f"Here is your {selection}. Would you like something else?\nYes/No\n").lower()