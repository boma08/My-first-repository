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

money = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def brew_coffee(coffee_type, coffee_ingredients):
    """Update the resources dictionary after processing order"""
    for item in coffee_ingredients:
        resources[item] -= coffee_ingredients[item]
    print(f"Here is your {coffee_type}, enjoy.")


def sufficient_funds(money_received, cost_of_drink):
    """Returns TRUE if the payment is sufficient to purchase the drink; FALSE if not"""
    global money
    if money_received >= cost_of_drink:
        money += cost_of_drink
        change = round(money_received - cost_of_drink, 2)
        print(f"Here is ${change} in change.")
        return True
    else:
        print(f"Sorry, ${money_received} is insufficient for a ${cost_of_drink} {coffee_choice}")
        return False


def enough_resources(coffee_ingredients):
    """Returns TRUE if the ingredients are enough to make the coffee; returns FALSE if not."""
    for item in coffee_ingredients:
        if coffee_ingredients[item] >= resources[item]:
            print(f"Sorry, there is not enough {item}")
            return False
    return True


def calculate_coins():
    """Returns the total amount in $ of coins inserted"""
    print("Please insert coins. ")
    total = int(input("How many Pennies?: ")) * 0.01
    total += int(input("How many Nickels?: ")) * 0.05
    total += int(input("How many Dimes?: ")) * 0.1
    total += int(input("How many Quarters?: ")) * 0.25
    return total


is_on = True
while is_on:
    coffee_choice = input("What would you like? ").lower()
    if coffee_choice == "off":
        is_on = False
    elif coffee_choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}ml")
        print(f"Money: ${money}")
    else:
        coffee = MENU[coffee_choice]
        if enough_resources(coffee['ingredients']):
            coffee_payment = calculate_coins()
            if sufficient_funds(coffee_payment, coffee['cost']):
                brew_coffee(coffee_choice, coffee['ingredients'])
