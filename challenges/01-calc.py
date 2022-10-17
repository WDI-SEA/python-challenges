# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.

operator = input('What calculation would you like to do? (add, sub, mult, div): ')
print(operator)
num1 = int(input('What is number 1? '))
print(num1)
num2 = int(input('What is number 2? '))
print(num2)
### MY WAY ###
# def maths(num1, num2):
#     res = ''
#     if operator == 'add':
#         res = int(num1) + int(num2)
#     elif operator == 'sub':
#         res = int(num1) - int(num2)
#     elif operator == 'mult':
#         res = int(num1) * int(num2)
#     elif operator == 'div':
#         res = int(num1) / int(num2)
#     else:
#         print('invalid operator. Please use + - * or /')
#     return res 

operations = {
    "add": num1 + num2,
    "sub": num1 - num2,
    "mult": num1 * num2,
    "div": num1 / num2,
}

if operator in operations:
    print(f'result {operations[operator]}')
else:
    print(f'{operator} is not a valid math.')

# print(f'The result of {num1} {operator} {num2} is {maths(num1, num2)}')