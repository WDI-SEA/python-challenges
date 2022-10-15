# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.

from ast import operator
from importlib.resources import open_binary


num_one = int(input("enter first number"))
num_two = int(input("enter second number"))
operator = input("choose your operator")

def calculate():
    if operator == "+":
        print (num_one + num_two )
    elif operator == "-":
        print (num_one - num_two)
    elif operator == "*" or operator =="x":
        print (num_one * num_two)
    elif operator == "/":
        print (num_one / num_two)

calculate()
