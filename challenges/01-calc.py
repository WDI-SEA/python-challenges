# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.

prompt = '> '
print('Enter calculation method: add, subtract, multiply, divide')
calc = input(prompt)
print(calc)
print ('Enter first number')
num1 = int(input(prompt))
print ('Enter second number')
num2 = int(input(prompt))
print(f'user input: calc {calc}, num 1: {num1}, num 2: {num2}')

operations = {
    "add": num1 + num2,
    "subtract": num1 - num2,
    "multiply": num1 * num2,
    "divide": num1 / num2
}

if calc in operations:
    print(f'result: {operations[calc]}')
else:
    print(f'{math} is not a valid math')
