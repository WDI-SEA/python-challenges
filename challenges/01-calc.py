# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.


# What calculation would you like to do? (add, sub, mult, div)
# add
# What is number 1?
# 3
# What is number 2?
# 6
# Your result is 9

use_method = input("What calculation would you like to do? ")
print(use_method)

add = '+'
subtract = '-'
divide = '/'
multiply = '*'

use_numberone = int(input("What is number 1? "))
print(use_numberone)
use_numbertwo = int(input("What is number 2? "))
print(use_numbertwo)

if use_method == 'add':
    print(f"Your result is: {((use_numberone) + (use_numbertwo))}")
elif use_method== 'subtract':
    print(f"Your result is: {((use_numberone) - (use_numbertwo))}")
elif use_method== 'multiply':
    print(f"Your result is: {((use_numberone) * (use_numbertwo))}")
elif use_method== 'divide':
    print(f"Your result is: {((use_numberone) / (use_numbertwo))}")