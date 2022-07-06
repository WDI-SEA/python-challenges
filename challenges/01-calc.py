# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.

function = input("What function would you like to do? (add, subtract, multiply, divide)")
print(function)
num1 = input("What is number 1?")
print(num1)
num2 = input("What is number 2?")
print(num2)

if (function == "add"):
    result = int(num1) + int(num2)
elif (function == "subtract"):
    result = int(num1) - int(num2)
elif (function == "multiply"):
    result = int(num1) * int(num2)
elif (function == "divide"):
    result = int(num1) / int(num2)
else:
    result = "nothing because you didnt pick an operation ya dork"

print("the result is", result)

# second solution method

def calc():
    operation = input("What kind of calculation do you want to make?\n")
    # print(operation)
    num1 = int(input("What is number 1?\n"))
    num2 = int(input("What is number 2?\n"))
    # print(num1, num2)

    methods = {
        "add": num1 + num2,
        "mult": num1 * num2,
        "div": num1 / num2,
        "sub": num1 - num2
    }

    if (operation in methods):
        return methods[operation]
    else: 
        return print("that's not good math. Try again!")

print(calc())