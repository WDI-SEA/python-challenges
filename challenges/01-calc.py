# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.

def calc():
    op = input('What calculation would you like to do? (add, sub, mult, div)\n')
    num1 = int(input('What is number 1?\n'))
    num2 = int(input('What is number 2?\n'))
    if (op == 'add'):
        print(f'Your result is {num1 + num2}')
    elif (op == 'sub'):
        print(f'Your result is {num1 - num2}')
    elif (op == 'mult'):
        print(f'Your result is {num1 * num2}')
    elif (op == 'div'):
        print(f'Your result is {num1 / num2}')

    
calc()