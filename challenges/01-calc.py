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