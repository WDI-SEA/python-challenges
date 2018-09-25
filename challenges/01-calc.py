# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.

def calc(method):
  if method == 'add':
    add_num1 = int(input('what is your first number?'))
    add_num2 = int(input('what is your second number?'))
    print(add_num1 + add_num2)
  elif method == 'sub':
    sub_num1 = int(input('what is your first number?'))
    sub_num2 = int(input('what is your second number?'))
    print(sub_num1 - sub_num2)
  elif method == 'multi':
    multi_num1 = int(input('what is your first number?'))
    multi_num2 = int(input('what is your second number?'))
    print(multi_num1 * multi_num2)
  elif method == 'div':
    div_num1 = int(input('what is your first number?'))
    div_num2 = int(input('what is your second number?'))
    print(div_num1 / div_num2)
  else:
    print('wut?')


print(calc(input('what would you like to do, add, sub, multi, div?')))
