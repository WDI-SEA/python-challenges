# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.

method = input('What calculator method would you like to use? (add, subtract, multiply, divide) ')
num1 = int(input('Enter first number '))
num2 = int(input('Enter second number '))

if method == 'add':
    result = num1 + num2
elif method == 'subtract':
    result = num1 - num2
elif method == 'multiply':
    result = num1 * num2
elif method == 'divide':
    result = num1/num2
else:
    result = 'cannot compute inputs, please try again'


print('Your result is', result)