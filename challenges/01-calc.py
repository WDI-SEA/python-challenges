# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.

def add(num1, num2):
    return num1 + num2

def sub(num1, num2):
    return num1 - num2

def mult(num1, num2):
    return num1 * num2

def div(num1, num2):
    return num1 / num2

math = input('What caluculation would you like to do? (add, subtract, multiply, divide) ')
num1 = int(input('Choose your first number: '))
num2 = int(input('Choose your second number: '))
if math == 'add':
    print(add(num1, num2))
elif math == 'subtract':
    print(sub(num1, num2))
elif math == 'multiply':
    print(mult(num1, num2))
elif math == 'divide':
    print(div(num1, num2))