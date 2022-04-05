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

prompt = '>'
print('Hello User, what math operation would you like to do?')
operator = input(prompt)
print('Hello User, please enter the first number')
number_1 = int(input(prompt))
print('Hello User, please enter the second number')
number_2 = int(input(prompt))
if operator == '+':
    result = number_1 + number_2
elif operator == '-':
    result = number_1 - number_2    
elif operator == '/':
    result = number_1 / number_2    
elif operator == '*':
    result = number_1 * number_2    
elif operator == '**':
    result = number_1 ** number_2    
print(f'The result is {result}')