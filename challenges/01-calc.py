# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.

print('What calculation would you like to do? (add, sub, mult, div')
x = input()
print('What is the first number?')
y = input()
print('What is the second number?')
z = input('')
if x == 'add':
    print('The rusult of ', y, 'plus ' , z, 'is ', float(y) + float(z))
elif x == 'sub':
    print('The rusult of ', y, 'minus ' , z, 'is ', float(y) - float(z))
elif x == 'mult':
    print('The rusult of ', y, 'multiplied by ', z, 'is ', float(y) * float(z))
elif x == 'div':
    print('The rusult of ', y, 'divided by ', z, 'is ', float(y) / float(z))
