# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.

calculation = input('What calculation would you like to do? (add, sub, mult, div): ')
num1 = int(input('First number: '))
num2 = int(input('Second number: '))

if calculation == 'add':
    print(f'Your result is: {num1 + num2}')
elif calculation == 'sub':
    print(f'Your result is: {num1 - num2}')
elif calculation == 'mult':
    print(f'Your result is: {num1 * num2}')
elif calculation == 'div':
    print(f'Your result is: {num1 / num2}') 