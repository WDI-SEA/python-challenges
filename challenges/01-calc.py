# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.

method = input('What calculation would you like to do? (add, sub, mult, div)?')
x = input('What is number 1?')
y = input('What is number 2?')

if (method == 'add'):
    print(int(x)+int(y))
elif (method == 'sub'):
    print(int(x)-int(y))
elif (method == 'mult'):
    print(int(x)*int(y))
else:
    print(int(x)/int(y))
