# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.


operator = input('What calculation would you like to do? (add, sub, mult, div) ')
number1 = input('What is your first number? (Enter a number) ')
number2 = input('What is your second number? (Enter a number) ')

def calc(operator, number1, number2):
    if operator == 'add':
        solution = int(number1) + int(number2)
    elif operator == 'sub':
        solution = int(number1) - int(number2)
    elif operator == 'mult':
        solution = int(number1) * int(number2)
    elif operator == 'div':
        solution = int(number1) / int(number2)
    else: 
        solution = 'Enter a valid operator'
    print(solution)
calc(operator, number1, number2)

