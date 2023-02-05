# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.


# define arithmetic functions first
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b
# then ask the user what they want to do
operation = input("What calculation would you like to do? (add, sub, mult, div)\n")
# then ask the user for the numbers for the calculation
number1 = int(input("What is number 1?\n"))
number2 = int(input("What is number 2?\n"))
# then do the calculation for each operation
if operation == 'add':
    result = add(number1, number2)
elif operation == 'sub':
    result = subtract(number1, number2)
elif operation == 'mult':
    result = multiply(number1, number2)
elif operation == 'div':
    result = divide(number1, number2)
else:
    result = None
    print("Invalid operation.")
# then print the result
if result is not None:
    print("Your result is", result)
