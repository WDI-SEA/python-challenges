# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.

operator = input("What calculation would you like to do? (add, sub, mult, div) ")
first_num = int(input("What is number 1: "))
second_num = int(input("What is number 2: "))

if operator == "add":
    print(first_num + second_num)
elif operator == "sub":
    print(first_num - second_num)
elif operator == "mult":
    print(first_num * second_num)
elif operator == "div":
    print(first_num / second_num)
else:
    print("Incorrect input")



