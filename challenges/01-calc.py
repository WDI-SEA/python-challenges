# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.

# def print_something():
#   print("Tell me something to print")
#   print(input())

# print_something()

# Create a simple calculator that first asks the user what method they would like to use (addition, subtraction, multiplication, division) and then asks the user for two numbers, returning the result of the method with the two numbers. Here is a sample prompt:

# What calculation would you like to do? (add, sub, mult, div)
# add
# What is number 1?
# 3
# What is number 2?
# 6
# Your result is 9

def calc():
    print("What would you like to do? (add, sub, mult, div)")
    op = input()
    if op != "add" and op != "sub" and op != "mult" and op != "div": 
        print("try again")
        calc()
    else:
        print("what is number 1?")
        num1 = int(input())
        print("what is number 2?")
        num2 = int(input())
        if op == "add":
            result = num1 + num2
        elif op == "sub":
            result = num1 - num2
        elif op == "mult":
            result = num1 * num2
        else
            result = num1 / num2
    print(f"your result is {result}!")

calc()