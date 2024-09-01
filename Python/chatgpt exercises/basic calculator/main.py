# Write a Python program that functions as a basic calculator. The program should be able to perform the following operations:
#
# Addition (+)
# Subtraction (-)
# Multiplication (*)
# Division (/)
# Requirements:
# Ask the user to input two numbers.
# Ask the user to select an operation (addition, subtraction, multiplication, or division).
# Perform the selected operation on the two numbers.
# Display the result.
# Operation methods
def add(num1, num2):
    return num1 + num2

def mult(num1, num2):
    return num1 * num2

def subtract(num1, num2):
    return num1 - num2

def div(num1, num2):
    # Handle ZeroDivisionError manually
    while num2 == 0:
        print("Error! Can not divide by zero (0). Please ensure the second number is not zero (0)")
        num2 = float(input("Enter second number: "))
    return num1 / num2

# Main loop for calculator
perform_calculation = input("Would you like to perform a calculation? enter Y/N: ").lower()

while perform_calculation == "y":
    # Handle invalid input error manually
    try:
        first_num = float(input("Enter first number: "))
        second_num = float(input("Enter second number: "))
    except ValueError:
        print("Invalid input! Please enter only numerical values.")
        continue

    # Map operators to functions
    operations = {
        "+": add,
        "-": subtract,
        "*": mult,
        "/": div
    }

    # Handle invalid operator scenarios
    while True:
        operator = input("Choose an operator(+, -, *, /): ")
        if operator in operations:
            # Perform calculation if operator is valid and exit loop
            print(f"Your answer is: {operations[operator](first_num, second_num)}")
            break
        else:
            print("Invalid operator selected. Please choose a valid operator.")

    # Continue or end calculator loop
    perform_calculation = input("Would you like to perform another calculation? enter Y/N: ").lower()

print("Thanks for using our app. Goodbye!")
