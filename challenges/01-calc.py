# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.

user_operation = input('What calculation would you like to do? (add, sub, mult, div) ')
number1 = int(input('What is your first number? '))
number2 = int(input('What is your second number? '))

if user_operation == 'add':
    result = number1+number2
elif user_operation == 'sub':
    result = number1-number2
elif user_operation == 'mult':
    result = number1*number2
elif user_operation == 'div':
    result = number1/number2
else:
    result='You cannot do that here. Try again'

print(f'Your result is {result}.')
