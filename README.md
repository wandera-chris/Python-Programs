# Python-Programs
Intro to Python Assignment
Instructions:

Basic Calculator Program

Create a simple Python program that asks the user to input two numbers and a mathematical operation (addition, subtraction, multiplication, or division).
Perform the operation based on the user's input and print the result.
Example: If a user inputs 10, 5, and +, your program should display 10 + 5 = 15.



Note: Upload the code to GitHub and submit the GitHub link

ANSWERS
def simple_calculator():
    """
    A simple calculator that takes two numbers and an operator as input
    and performs the corresponding mathematical operation.
    """
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operator = input("Enter the operator (+, -, *, /): ")

        if operator == '+':
            result = num1 + num2
            print(f"{num1} + {num2} = {result}")
        elif operator == '-':
            result = num1 - num2
            print(f"{num1} - {num2} = {result}")
        elif operator == '*':
            result = num1 * num2
            print(f"{num1} * {num2} = {result}")
        elif operator == '/':
            if num2 == 0:
                print("Error: Division by zero is not allowed.")
            else:
                result = num1 / num2
                print(f"{num1} / {num2} = {result}")
        else:
            print("Invalid operator. Please enter +, -, *, or /.")

    except ValueError:
        print("Invalid input. Please enter numbers.")

simple_calculator()
