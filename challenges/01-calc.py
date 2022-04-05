# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.

operator = input('What calculation would you like to do? (add, subtract, multiply, or divide): ')
num1 = int(input('Enter your first Number: '))
num2 = int(input('Enter your second Number: '))

if operator == 'add':
  print(f'Your result of adding is {num1 + num2}')
elif operator == 'subtraction':
  print(f'Your result of subtracting is {num1 - num2}')
elif operator == 'multiply':
  print(f'Your result of multiplying is {num1 * num2}')
elif operator == 'divide':
  print(f'Your result of dividing is {num1/num2}')
else:
  print('error, please try again')