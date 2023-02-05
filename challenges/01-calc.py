# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.
import sys

calc_type = input('What calculation would you like to do? (add | sub | mult | div)')

match calc_type:
  case 'add' | 'sub' | 'mult' | 'div':
    pass
  case _:
    print('Calculation must match one of the following words: add, sub, mult, or div')
    sys.exit()
    

num_1 = int(input('What is the first number?'))

num_2 = int(input('What is the second number?'))

def add(num1, num2):
  result = num1 + num2
  print(f'Your result is {result}')
  
def sub(num1, num2):
  result = num1 - num2
  print(f'Your result is {result}')
  
def mult(num1, num2):
  result = num1 * num2
  print(f'Your result is {result}')
  
def div(num1, num2):
  result = num1 / num2
  print(f'Your result is {result}')

match calc_type:
  case 'add':
    add(num_1, num_2)
  case 'sub':
    sub(num_1, num_2)
  case 'mult':
    mult(num_1, num_2)
  case 'div':
    div(num_1, num_2)