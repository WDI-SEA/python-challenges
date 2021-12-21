# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.

## sample input prompts
# What calculation would you like to do? (add, sub, mult, div)
# add
# What is number 1?
# 3
# What is number 2?
# 6
# Your result is 9

op = input("What calculation would you like to do? (add, sub, mult, div)")
num1 = int(input("What is number 1?"))
num2 = int(input("What is number 2?"))

# Python 3.10 and above only
# match "add":
#     case "add":
#         return num1 + num2
#     case "sub":
#         return num1 - num2
#     case "mult":
#         return num1 * num2
#     case "div":
#         return num1 / num2

if op == "ad":
    print("Your result is: ", num1 + num2)
if op == "sub":
    print("Your result is: ", num1 - num2)
if op == "mult":
    print("Your result is: ", num1 * num2)
if op == "div":
    print("Your result is: ", num1 / num2)