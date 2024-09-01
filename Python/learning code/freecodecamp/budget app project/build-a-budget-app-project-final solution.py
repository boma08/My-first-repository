class Category:

    def __init__(self, category):
        self.category = category
        self.ledger = []
        self.balance = 0

    def display_category(self):
        display = ""
        display += f"{self.category.center(30, '*')}\n"
        for expense in self.ledger:
            display += expense["description"][:23].ljust(23) + str("%.2f" % expense["amount"])[:7].rjust(7)
            display += "\n"
        display += f"Total: " + str(self.balance)
        return display

    def __str__(self):
        return self.display_category()

    def check_funds(self, amount):
        if amount > self.balance:
            return False
        else:
            return True
    
    def deposit(self, amount, description = ""):
        self.balance += amount 
        self.ledger.append(
            {
            "amount" : amount,
            "description" : description
            }
            )

    def withdraw(self, amount, description = ""):
        if self.check_funds(amount):
            self.ledger.append(
                {
                "amount" : amount * -1,
                "description" : description
                }
                )
            self.balance -=amount
            return True
        else:
            return False

    def transfer(self, amount, cate):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {cate.category}")
            cate.deposit(amount, f"Transfer from {self.category}")
            return True
        else: return False

    def get_balance(self):
        return self.balance
    
      

def create_spend_chart(categories):
    chart = ""
    def get_withdrawal(category):
        withdrawal = 0
        for i in range(len(category.ledger)):
                if category.ledger[i]["amount"] < 0:
                    withdrawal += category.ledger[i]["amount"]
        return abs(withdrawal)

    def print_bar(dictionary, percentage):
        line = ""
        for item in dictionary:
            if percentage > dictionary[item]:
                line += "   "
            elif percentage <= dictionary[item]:
                line += "o  "
        return line


    withdrawal_dict = {
        cat.category: get_withdrawal(cat) for cat in categories
    }

    percentage_spent = {
        key: (value * 100) / sum(withdrawal_dict.values()) for key, value in withdrawal_dict.items()
    }


    chart += "Percentage spent by category\n"
    for percentage in range(100, -10, -10):
        chart += (str(percentage) + "|").rjust(4) + " " + print_bar(percentage_spent, percentage) + "\n"
    dash_length = (len(categories) * 3) + 1 
    dashes = "    "
    for _ in range(dash_length):
        dashes += "-" 
    chart += dashes + "\n"


    index = 0
    cat = [len(item.category) for item in categories]
    
    while index < max(cat):
        line = "     "
        for item in categories:
            if item.category[-1] == item.category[0] and len(item.category) == 1:
                if item.category == "_":
                    line += " "
                else:
                    line += item.category[index]
                    item = "_" 
            else:
                try: 
                   line += item.category[index] + "  "
                except IndexError:
                    line += "   "
        index += 1
        chart += line + "\n"
    chart = chart[:-1]
    return chart
        



categories = []
food = Category("Food")
clothing = Category("Clothing")
home = Category("Hommie")
edu = Category("Educationiskey")

food.deposit(1000, "deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
food.transfer(50, clothing)
food.transfer(150, home)

home.deposit(200, "deposit")
home.withdraw(20, "furniture")
home.withdraw(30, "kitchenware")
home.transfer(40, edu)

edu.deposit(300, "initial deposit")
edu.withdraw(150, "books")
edu.withdraw(20, "sch uniform")
edu.transfer(20, clothing)

clothing.withdraw(15, "shoes")

categories.append(food)
categories.append(clothing)
categories.append(home)
categories.append(edu)

print(food)
print(create_spend_chart(categories))



