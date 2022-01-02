# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.

operation = input('what calculation would you like to do? (add, sub, mult, div)\n')
num1 = int(input('what is number 1? \n'))
num2 = int(input('what is number 2?\n'))

if operation == 'add':
    result = (num1 + num2)
    print(f'Your result is {result}')
elif operation == 'sub':
    result = (num1 - num2)
    print(f'Your result is {result}')
elif operation == 'mult':
    result = (num1 * num2)
    print(f'Your result is {result}')
elif operation == 'div':
    result = (num1 / num2)
    print(f'Your result is {result}')
else:
    print('invalid operator')






