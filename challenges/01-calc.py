# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.


num1 = int(input('1st Number: '))
num2 = int(input('2nd Number: '))
method = input('What calculation would you like to do? (add, sub, mult, div): ')

if(method == 'add'):
    print(num1 + num2)
elif(method == 'sub'):
    print(num1 - num2)
elif(method == 'mult'):
    print(num1 * num2)
else:
    print(num1 / num2)


