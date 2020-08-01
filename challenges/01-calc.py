# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.

operation = input("What operation would you like to do today?")
num1 = input("What is the first number?")
num2 = input("What is the second number?")
if operation == "add":
    print (float(num1) + float(num2))
elif operation == "subtract":
    print (float(num1) - float(num2))
elif operation == "multiply":
    print (float(num1) * float(num2))
elif operation == "divide":
    print (float(num1) / float(num2))
else:
    print("I don't know how to do that")