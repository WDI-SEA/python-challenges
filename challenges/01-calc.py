# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.

operator = input("What calculation would you like to do? (add, sub, mult, div)\n")
num1 = input("What is number 1?\n")
num2 = input("What is number 2?\n")

# match case (python 3.10+)
# match operator:
#     case "add":
#         print(f"Your result is {int(num1) + int(num2)}")
#     case "sub":
#         print(f"Your result is {int(num1) - int(num2)}")
#     case "mult":
#         print(f"Your result is {int(num1) * int(num2)}")
#     case "div":
#         print(f"Your result is {int(num1) / int(num2)}")
#     case other:
#         print("Invalid operator")

# if-else
if operator == "add":
    print(f"Your result is {int(num1) + int(num2)}")
elif operator == "sub":
    print(f"Your result is {int(num1) - int(num2)}")
elif operator == "mult":
    print(f"Your result is {int(num1) * int(num2)}")
elif operator == "div":
    print(f"Your result is {int(num1) / int(num2)}")
else:
    print("Invalid operator")
