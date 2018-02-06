# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.
def calc(str, num1, num2):
  switcher = {
    'add': num1 + num2,
    'sub': num1 - num2,
    'mult': num1 * num2,
    'div': num1 / num2,
    'mod': num1 % num2, 
  }
  return switcher.get(str, 'Invalid operation selection')

method_str = input('add, sub, mult, div, mod: ')
num1 = input('What is the first nubmer: ')
num2 = input('What is the second number: ')

try:
  num1 = int(num1)
  num2 = int(num2)
except:
  print('Both values should be numeric. Please try again.')

print(calc(method_str, num1, num2))