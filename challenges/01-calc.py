# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.


operation = input('What calculation would you like to do (add, sub, mult, div)? ')
num_one = int(input('What is number 1? '))
num_two = int(input('What is number 2? '))

if operation == 'add':
    print(num_one + num_two)
elif operation == 'sub':
    print(num_one - num_two)
elif operation == 'mult':
    print(num_one * num_two)
elif operation == 'div':
    print(num_one / num_two)

