# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.

# Create a simple calculator that first asks the user what method they would like to use (addition, subtraction, multiplication, division) and then asks the user for two numbers, returning the result of the method with the two numbers. Here is a sample prompt:

# What calculation would you like to do? (add, sub, mult, div)
# add
# What is number 1?
# 3
# What is number 2?
# 6
# Your result is 9

user_input = input('What method would you like to use (addition, subtraction, multiplication, division)?')
num1 = int(input('What is number 1?'))
num2 = int(input('What is number 2?'))

if user_input == 'addition':
    result = (num1 + num2)
    print(f'Your result is {result}')
elif user_input == 'subtraction':
    result = (num1 - num2)
    print(f'Your result is {result}')
elif user_input == 'multiplication':
    result = (num1 * num2)
    print(f'Your result is {result}')
elif user_input == 'division':
    result = (num1 / num2)
    print(f'Your result is {result}')
else:
    print('Invalid input')