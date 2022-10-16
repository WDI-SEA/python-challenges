# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.

from ast import Num


user_selection = input('What operation would you like to perform? (add, sub, mult, div): \n')
print(user_selection)
num_one = int(input('What is the first number?: \n'))
print(num_one)
num_two = int(input('What is the second number?: \n'))
print(num_two)

def calculate(num_one, num_two):
    if user_selection == 'add':
        print('The total after adding is', num_one + num_two)
    elif user_selection == 'sub':
        print('The total after subtracting is', num_one - num_two)
    elif user_selection == 'mult':
        print('The total after multiplying is', num_one * num_two)
    elif user_selection == 'div':
        print('The total after dividing is', num_one / num_two)

calculate(num_one, num_two)
