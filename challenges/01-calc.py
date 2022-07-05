# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.

valid = False
method = None
num1 = None
num2 = None

while not valid:
  method = input("What method do you want to do? (add, sub, mul, div): ")
  valid = method in ['add', 'sub', 'mul', 'div']
  if not valid: print("Invalid method. Please try again.")


is_num_1_valid = False
while not is_num_1_valid:  
  try:
    num1 = int(input("What is number 1? "))
    is_num_1_valid = True
  except:
    print('Invalid number. Please try again.')
    is_num_1_valid = False

is_num_2_valid = False
while not is_num_2_valid:  
  try:
    num2 = int(input("What is number 2? "))
    is_num_2_valid = True
  except:
    print('Invalid number. Please try again.')
    is_num_2_valid = False

try:
  if method == 'add':
    result = num1 + num2
  elif method == 'sub':
    result = num1 - num2
  elif method == 'mul':
    result = num1 * num2
  elif method == 'div':
    result = num1 / num2
except ZeroDivisionError:
  print("Uh. oh. Division by zero.")
  exit()
except:
  print("Something went wrong.")
  exit()

print('Your result is', result)