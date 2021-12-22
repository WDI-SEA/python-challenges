# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.

def simple_calc():

    result = 0

    print('What calculation would you like to do? (add, sub, mult, div)')
    calc_input = input()

    print('What is number 1?')
    number1_input = input()

    print('What is number 2?')
    number2_input = input()

    if calc_input == 'add':
        result = int(number1_input) + int(number2_input)
    elif calc_input == 'sub':
        result = int(number1_input) - int(number2_input)
    elif calc_input == 'mult':
        result = int(number1_input) * int(number2_input)
    elif calc_input == 'div':
        result = int(number1_input) / int(number2_input)

    print(result)
simple_calc()
