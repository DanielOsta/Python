from typing import Dict

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

profit = 0
resources: dict[str, int] = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def print_report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: {profit}$")


def is_resource_sufficient(order_ingredients) -> bool:
    for item in order_ingredients:
        if order_ingredients[item] > resources['water']:
            print('Sorry there is not enough water.')
            return False
    return True


def process_coins(cost) -> float:
    print(f"Cost: {cost}$. Insert coins.")
    quarters = int(input('Quarters : '))
    dimes = int(input('Dimes : '))
    nickles = int(input('Nickles : '))
    pennies = int(input('Pennies : '))
    total = round(quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01, 2)
    return total


def is_transaction_successful(money_received, cost) -> bool:
    if money_received < cost:
        print("Sorry that's not enough money. Money refunded.")
        return False
    else:
        diff = round(money_received - cost, 2)
        print(f"Here is ${diff} dollars in change.")
        global profit
        profit += cost
        return True


def make_coffee(ingredients):
    resources['water'] -= ingredients['water']
    if 'milk' in ingredients:
        resources['milk'] -= ingredients['milk']
    resources['coffee'] -= ingredients['coffee']


is_on = True

while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino):")
    if choice == 'off':
        print("Turning off the coffee machine.")
        is_on = False
    elif choice == 'report':
        print_report()
    elif choice == 'espresso' or choice == 'latte' or choice == 'cappuccino':
        drink = MENU[choice]
        if is_resource_sufficient(drink['ingredients']):
            inserted_coins = process_coins(drink['cost'])
            if is_transaction_successful(inserted_coins, drink['cost']):
                make_coffee(drink['ingredients'])
                print(f'Here is your {choice}. Enjoy!')


