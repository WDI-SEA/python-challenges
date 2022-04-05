# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.
calc = input('What calculation would you like to do? (add, sub, mult, div')
first = input('please input the first number')
second = input('please input the second number')
if calc == 'add':
    print(f'your result is {first} + {second} = {int(first) + int(second)}')
elif calc == 'subtract':
    print(f'your result is {first} - {second} = {int(first) - int(second)}')
elif calc == 'mult':
    print(f'your result is {first} * {second} = {int(first) * int(second)}')
elif calc == 'div':
    print(f'your result is {first} / {second} = {int(first) / int(second)}')
    