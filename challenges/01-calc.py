# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.


ask = (input("What would you like to do? (add, sub, mult, div)"))
x = int(input("Enter number 1: "))
y = int(input("Enter number 2: "))
if(ask == 'add'):
    print(x + y)
elif(ask == 'sub'):
    print(x - y)
elif(ask == 'mult'):
    print(x * y)
else:
    print(x // y)
