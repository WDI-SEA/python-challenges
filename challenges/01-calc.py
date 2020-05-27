# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.

operator = {'add': '+', 'sub': '-', 'mult': '*', 'div': '/'}

op_input = input('What calculation would you like to do? (add, sub, mult, div) ')

print(op_input)

# op_func = operator.get(op_input)

# print(op_func)

num1 = input('What is number 1? ')

print(num1)

num2 = input('What is number 2? ')

print(num2)

def calculator(operator, num1, num2):
    num1_int = int(num1)
    num2_int = int(num2)
    if op_input == 'add':
        return num1_int + num2_int
    elif op_input == 'sub':
        return num1_int - num2_int
    elif op_input == 'mult':
        return num1_int * num2_int
    elif op_input == 'div':
        return num1_int / num2_int
    else:
        return print('Make valid inputs') 

print(calculator(op_input, num1, num2))