# Use the `input()` function to prompt a user to enter something.
operation = input('Would you like to add, subtract, multiply, or divide?')

# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.
num1 = int(input('Number 1: '))
num2 = int(input('Number 2: '))

if operation == 'add':
    print(num1 + num2)
elif operation == 'sub':
    print(num1 - num2)
elif operation == 'mult':
    print(num1 * num2)
elif operation == 'div':
    print(num1 / num2)
else:
    print('error, try again!')