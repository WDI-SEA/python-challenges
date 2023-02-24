# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.
# Create a simple calculator that first asks the user what method they would like
# to use (addition, subtraction, multiplication, division) and then asks the user
# for two numbers, returning the result of the method with the two numbers. Here
# is a sample prompt:

# ```
# What calculation would you like to do? (add, sub, mult, div)
# add
# What is number 1?
# 3
# What is number 2?
# 6
# Your result is 9

method = input('What math do you want to do today (add, sub, mult, div)?  ')
firstnum = int(input('What is your first number?  '))
secondnum = int(input('What is your second number?  '))

def calculator(meth, first, second):
    if meth.lower() not in ('add', 'sub', 'mult', 'div'):
        print('sorry, response invalid, please choose a proper method')
    elif (meth == 'add'):
        return first + second
    elif (meth == 'sub'):
        return first - second
    elif (meth == 'mult'):
        return first * second
    else:
        return first / second


print('your result is', calculator(method, firstnum, secondnum))



