# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.

calculation = input('What calculation would you like to do? (add, sub, mult, div) ')
number_one = int(input('What is number 1? '))
number_two = int(input('What is number 2? '))
total = 'total'

if calculation == 'add':
    total = number_one + number_two
elif calculation == 'sub':
    total = number_one - number_two
elif calculation == 'mult':
    total = number_one * number_two
elif calculation == 'div':
    total = number_one / number_two
else:
    total = 'Please enter a proper calculation (add, sub, mult, or div)'

print(f'Your result is {total}')