# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.


user = input('Add, Subtract, Multiply, or Divide')

num1 = input('Value 1')

num2 = input ('Value 2')

if (user == 'add'):
    result = int(num1) + int(num2)
if (user == 'subtract'):
    result = int(num1) - int(num2)
if (user == 'multiply'):
    result = int(num1) * int(num2)
if (user == 'divide'):
    result = int(num1) / int(num2)



input(f'{result}')