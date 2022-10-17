# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.

def calculator():
    # get all user input
    method = input("what method would youlike to use?\n")

    # get number from user
    x = int(input("what is number 1?\n"))
    y = int(input("what is number 2?\n"))

    methods = {
        "add": x + y,
        "multiply": x * y,
        "div": x / y,
        "sub": x - y,
    }

    if (method in methods):
        return methods[method]
    else:
        return print ("Argh - you did not give a correct metho! Try again.")

print(calculator())