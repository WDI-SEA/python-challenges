# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.

operation =''

while operation not in ['add','sub','mult','div']:
    operation = input('What calculation would you like to do? (add, sub, mult, div)\n')

num_1 = int(input('What is number 1?'))
num_2 = int(input('What is number 2?'))

if operation == 'add':
    print(int(num_1 + num_2))
elif operation == 'sub':
    print(int(num_1 - num_2))
elif operation == 'mult':
    print(int(num_1 * num_2))
elif operation == 'div':
    print(int(num_1 / num_2))
