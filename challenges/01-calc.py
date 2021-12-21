# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.

operation = input('What would you like to do? (add, sub, mult, div): ')
num1 = int(input('What is number 1?: '))
num2 = int(input('What is number 2?: '))

if operation == 'add':
    print(num1 + num2)
elif operation == 'sub':
    print(num1 - num2)
elif operation == 'mult':
    print(num1 * num2)
elif operation == 'div':
    print(num1 / num2)
else:
    print('user error. try again!')