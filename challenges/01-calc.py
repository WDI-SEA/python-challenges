# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.

from ast import operator


prompt = '> '
print('Enter the operation you wish to use: add, sub, mult, div')
math = input(prompt)

print('Enter the first number')
input_one = input(prompt)
print('Enter the second number')
input_two = input(prompt)

calculate = {
  'add' : int(input_one) + int(input_two),
  'sub' : int(input_one) - int(input_two),
  'mult': int(input_one) * int(input_two),
  'div' : int(input_one) / int(input_two)
}

operation = {
  'add' : '+',
  'sub' : '-',
  'mult': '*',
  'div' : '/',
}

if math in operation:
  print(f'You calculated: {input_one} {operation[math]} {input_two} = {calculate[math]}')
else:
  print('Bad Input 🤨')