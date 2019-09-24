# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.

def do_math():
    method = input("What kind of math function would you like to do (add, sub, mult, div)?: ")
    num1 = int(input("What is number 1?: "))
    num2 = int(input("What is number 2?: "))

    result = 0
    if method == "add":
        result = num1 + num2
    elif method == "sub":
        result = num1 - num2
    elif method == "mult":
        result = num1 * num2
    elif method == "div":
        result = num1 / num2
    else:
        print(f"Sorry, I don't know that one: {method}")
        return
    print(f"Your result is {result}")
    return

do_math()
