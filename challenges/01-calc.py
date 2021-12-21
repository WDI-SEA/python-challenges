# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.
operate = input('What calculation would you like to do?(add, sub, mult, div) ')
num1 = int(input('What is number 1? '))
num2 = int(input('What is number 2? '))
def calculate(num1, num2):
    if operate == 'add':
            result = num1 + num2
            print('your result is ', result)
    elif operate == 'sub':
            result = num1 - num2
            print('your result is ', result)
    elif operate == 'mult':
            result = num1 * num2
            print('your result is ', result)
    elif operate == 'div':
            result = num1/num2
            print('your result is ', result)
calculate(num1, num2)