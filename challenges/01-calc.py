# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.

### EXAMPLE PROMPT:
# What calculation would you like to do? (add, sub, mult, div)
# add
# What is number 1?
# 3
# What is number 2?
# 6
# Your result is 9

calc = input("What calculation would you like to do? (add, sub, mult, div) ")

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

if calc == "add":
    a = int(input("What is number 1? "))
    b = int(input("What is number 2? "))
    print(add(a, b))

elif calc == "sub":
    a = int(input("What is number 1? "))
    b = int(input("What is number 2? "))
    print(subtract(a, b))

elif calc == "mult":
    a = int(input("What is number 1? "))
    b = int(input("What is number 2? "))
    print(multiply(a, b))

elif calc == "div":
    a = int(input("What is number 1? "))
    b = int(input("What is number 2? "))
    print(divide(a, b))

else:
    print("Please enter a valid calculation")



