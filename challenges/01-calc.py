# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.


oper = input('What would you like to do? ')
num1 = int(input('Enter first number '))
num2 = int(input('Enter second number '))

if oper == 'add':
    result = (num1 + num2)
elif oper == 'sub':
    result = (num1 - num2)
elif oper == 'mult':
    result = (num1 * num2)
elif oper == ('div'):
    result = (num1 / num2)
    print(result)
else:
    print('Please enter add, sub, mult or div ')

print(result)
