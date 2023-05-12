# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.

while True:

    operation = input("What operation would you like to do? Input add, sub, mult, or div: ")

    num1 = int(input("What's your first number? "))

    num2 = int(input("What's your second number? "))

    if operation == "add":
        print("Your result is " + str(num1 + num2))
    elif operation == "sub":
        print("Your result is " + str(num1 - num2))
    elif operation == "mult":
        print("Your result is " + str(num1 * num2))
    elif operation == "div":
        print("Your result is " + str(num1 / num2))
    