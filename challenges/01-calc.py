# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.
op = input('What calculation would you like to do? (add, sub, mult, div)')

num1 = input('What is number 1?')

num2 = input('What is number 2?')

if(op == 'add'):
    result = int(num1) + int(num2)
if(op == 'sub'):
    result = int(num1) - int(num2)
if(op == 'mult'):
    result = int(num1) * int(num2)
if(op == 'div'):
    result = int(num1) / int(num2)

input(f'Your result is {result}')