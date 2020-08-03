# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.
def calculator():
    method = input("What method would you like to use \n")

    x = int(input("what is number one \n"))
    y = int(input("what is number two \n"))
    
    methods = {
        "add" : x + y,
        "multiply": x * y,
        "div" : x / y,
        "subtract": x - y
    }

    if (method in methods):
        return print(methods[method])
    else: 
        return print("Incorrect method")

calculator()