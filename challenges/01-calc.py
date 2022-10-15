# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.

operator = input('What calculation would you like to do? (add, sub, mult, div): ')
print(operator)
num1 = input('What is number 1? ')
print(num1)
num2 = input('What is number 2? ')
print(num2)

def maths(num1, num2):
    res = ''
    if operator == '+':
        res = int(num1) + int(num2)
    elif operator == '-':
        res = int(num1) - int(num2)
    elif operator == '*':
        res = int(num1) * int(num2)
    elif operator == '/':
        res = int(num1) / int(num2)
    else:
        print('invalid operator. Please use + - * or /')
    return res 

print(f'The result of {num1} {operator} {num2} is {maths(num1, num2)}')