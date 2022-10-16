# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.


def calculator():
    operator = input('''
    Which math operator would you like to use?
    + for addition
    - for subtraction
    * for multiplication
    / for division

    your choice: 
    '''
    )

    operators = '+-*/'

    if (operator in operators):
        num_one = int(input('Enter your 1st Number: '))
        num_two = int(input('Enter your 2nd Number: '))

        if operator == '+':
            print(f'{num_one} + {num_two} = {num_one + num_two}')
        if operator == '-':
            print(f'{num_one} - {num_two} = {num_one - num_two}')
        if operator == '*':
            print(f'{num_one} * {num_two} = {num_one * num_two}')
        if operator == '/':
            print(f'{num_one} / {num_two} = {num_one / num_two}')
    else: 
        print('incorrect operator, try again.')


    

    

calculator()