# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.

prompt = '>'
print('What calculation would you like to do? (add, sub, mult, div)')
operation = input(prompt)
print('What is number 1?')
num1 = input(prompt)
print('What is number 2?')
num2 = input(prompt)

if operation == 'add':
    print(f'Your result is {int(num1) + int(num2)}')
elif operation == 'sub':
    print(f'Your result is {int(num1) - int(num2)}')
elif operation == 'mult':
    print(f'Your result is {int(num1) * int(num2)}')
elif operation == 'div':
    print(f'Your result is {int(num1) / int(num2)}')
else: 
    print('Invalid operation')
