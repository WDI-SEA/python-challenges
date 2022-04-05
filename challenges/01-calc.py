# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.

print('What calculation would you like to do? (add, sub, mult, div)')
operation = input()
print('What is the 1st number? ')
num1 = input()
print('What is the 2nd number?')
num2 = input()

if operation == 'add':
    print(f'Your result is: {int(num1) + int(num2)} ')
elif operation == 'sub':
    print(f'Your result is: {int(num1) - int(num2)}')
elif operation == 'mult':
    print(f'Your result is: {int(num1) * int(num2)}')
elif operation == 'div':
    print(f'Your result is: {int(num1) / int(num2)}')
