# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.

### Challenge 1 - Calculator

# Create a simple calculator that first asks the user what method they would like
# to use (addition, subtraction, multiplication, division) and then asks the user
# for two numbers, returning the result of the method with the two numbers. Here
# is a sample prompt:

# ```
# What calculation would you like to do? (add, sub, mult, div)
# add
# What is number 1?
# 3
# What is number 2?
# 6
# Your result is 9
# ```

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