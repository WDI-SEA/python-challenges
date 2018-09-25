# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.


operation = input('''
What calculation would you like to do? (add, sub, mult, div):
add
sub
mult
div
''')

number_1 = int(input('What is number 1? '))
number_2 = int(input('What is number 2? '))

if operation == 'add':
    print('{} + {} = '.format(number_1, number_2))
    print(number_1 + number_2)

elif operation == 'sub':
    print('{} - {} = '.format(number_1, number_2))
    print(number_1 - number_2)

elif operation == 'mult':
    print('{} * {} = '.format(number_1, number_2))
    print(number_1 * number_2)

elif operation == 'div':
    print('{} / {} = '.format(number_1, number_2))
    print(number_1 / number_2)

else:
    print('You have not typed a valid operator, please run the program again.')