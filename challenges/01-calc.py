# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.


def calculator():
    operator = input(
        'What calculation would you like to do: (add, sub, mult, div)? ')
    num1 = input('What is number 1? ')
    num2 = input('What is number 2? ')

    if operator == 'add':
        print('Your result is ', int(num1) + int(num2))
    elif operator == 'sub':
        print('Your result is ', int(num1) - int(num2))
    elif operator == 'mult':
        print('Your result is ', int(num1) * int(num2))
    elif operator == 'div':
        print('Your result is ', int(num1) / int(num2))


calculator()
