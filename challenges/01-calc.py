# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.

def do_math():
    method = input('what kinda math function you waana do? (add, sub, mult, div) \n')
    num1 = int(input('what is number1'))
    num2 =  int(input('what is number2'))
    result = 0
    if method == 'add':
        result = num1 + num2
    elif method == 'sub':
        result = num1 - num2
    elif method == 'mult':
        result = num1 * num2
    elif method == 'div':
        result = num1/num2
    else:
        print('no')
    print(f'resut is {result}')
