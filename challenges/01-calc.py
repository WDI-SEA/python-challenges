# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.

operation = input('What operation would you like to perform? Please enter add, sub, mult, or div: ')
num1 = int(input('Enter your first number: '))
num2 = int(input('Enter your second number: '))

if operation == 'add':
    print(f'Your result is {num1 + num2}')
elif operation == 'sub':
    print(f'Your result is {num1 - num2}')
elif operation == 'mult':
    print(f'Your result is {num1 * num2}')
elif operation == 'div':
    print(f'Your result is {num1 / num2}')