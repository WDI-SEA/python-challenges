# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.

from platform import java_ver


def calculator():
    # get the user input
    method = input("what method would you like to use for calcultion?")

    #get numbers from the user
    i = int(input("what is the first number?"))
    j = int(input("What is the second number?"))

    methods = {
        "add": i + j,
        "multiply": i * j,
        "div": i / j,
        "subtract": i - j
    }

    if (method in methods):
        return methods[method]
    else:
        return print("uggg - you did not give the correct method! again please")


print(calculator())