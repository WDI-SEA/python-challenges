# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.

def add(a, b):
    return a + b
    
def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

# input("What calculation would you like to do? (add, sub, mult, div) ")

operator = input("What calculation would you like to do? (add, sub, mult, div) ")
num1 = int(input("What is number 1? "))
num2 = int(input("What is number 2? "))


if operator == "add":
    print("Your result is:",(add(num1, num2)))
elif operator == "sub":
    print("Your result is:",(subtract(num1, num2)))
elif operator == "mult":
    print("Your result is:",(multiply(num1, num2)))
elif operator == "div":
    print("Your result is:",(divide(num1, num2)))
else:
    print("Please enter a valid operator")

# Path: challenges/02-bmi.py
# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.




