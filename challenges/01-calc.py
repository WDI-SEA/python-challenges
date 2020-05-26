# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.

method = input("add, subtract, multiply, or divide?")
num_1 = int (input("first number?"))
num_2 = int (input("second number?"))

if method == 'add':
  result = num_1 + num_2
  print(result)
elif method == 'subtract':
  result = num_1 - num_2
  print(result)
elif method == 'multiply':
  result = num_1 * num_2
  print(result)
elif method == 'divide':
  result = num_1 / num_2
  print(result)
else:
  print('error')