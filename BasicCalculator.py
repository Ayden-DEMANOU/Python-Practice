# 1. Basic Calculator (CLI: Command Line Interface)
# Input: two numbers and an operation
# Teaches: functions, conditionals, inputs, printing

""" We want a program that:
- Asks the user for two numbers
- Asks the user for an operation (+, -, *, /)
- Calculates the result
- Prints the result clearly
"""

"""
1. A function for each operation: add(a, b), subtract(a, b), multiply(a, b), divide(a, b) : For easy access and reusability.
2. A function that handles user input: get numbers, get operation
3. A function to run the calculator
"""

# Adding operation
def add(a,b):
    return a + b

# Subtraction Operation
def subtract(a, b):
    return a - b

# Multiplication Operation
def multiply(a, b):
    return a * b

# Division Operation
def divide(a, b):
    if b == 0:
        print("Error: Cannot divide by 0")
    else:
        return a / b


# CALCULATOR Function
def calculator():
    print("Welcome to the Basic CLI Calculator")

    # Getting the user inputs and the operation
    number1 = float(input("Enter the first number: "))
    number2 = float(input("Enter the second number: "))
    operation = input("Enter operation (+, -, *, /): ")

    # Use control flows to decide which function to call
    if operation == "+":
        result = add(number1, number2)
    elif operation == "-":
        result = subtract(number1, number2)
    elif operation == "*":
        result = multiply(number1, number2)
    elif operation == "/":
        result = divide(number1, number2)
    else: 
        result = "Invalid Operation!"

    print("Result:", result)


calculator()