# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.

def calc():
    operation = input("What calculation would you like to do? (add, sub, mult, div)\n")
    num1 = input("What is number 1?\n")
    num2 = input("What is number 2?\n")


    if(operation == "add"):
        result = int(num1) + int(num2)
    elif(operation == "sub"):
        result = int(num1) - int(num2)
    elif(operation == "mult"):
        result = int(num1) * int(num2)
    elif(operation == "div"):
        result = int(num1) / int(num2)
    else:
        result = "nothing because you did not choose a valid operation"

    print("Your result is", result)

calc()

def calc():
    operation = input("What calculation would you like to do? (add, sub, mult, div)\n")
    num1 = int(input("What is number 1?\n"))
    num2 = int(input("What is number 2?\n"))

    methods = {
        "add": num1 + num2,
        "sub": num1 - num2,
        "mult": num1 * num2,
        "div": num1 / num2
    }

    if(operation in methods):
        print

calc()