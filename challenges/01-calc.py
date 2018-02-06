# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.

# def request_input():
#   you = input("What is your name?")
#   color = input("What is your favorite color?")
#   print("Your name is {} and your favorite color is {}".format(you, color))

# request_input()

# Create a simple calculator that first asks the user what method they would like to use (addition, subtraction, multiplication, division) and then asks the user for two numbers, returning the result of the method with the two numbers. Here is a sample prompt:

# What calculation would you like to do? (add, sub, mult, div)
# add
# What is number 1?
# 3
# What is number 2?
# 6
# Your result is 9

def calculate():
  method = input("What calculation would you like to do? (add, sub, mult, div)")
  num1 = int(input("What is number 1?"))
  num2 = int(input("What is number 2?"))
  
  if method == 'add':
    print('{} + {} = '.format(num1, num2))
    print(num1 + num2)
  elif method == 'sub':  
    print('{} - {} = '.format(num1, num2))
    print(num1 - num2)
  elif method == 'mult':  
    print('{} * {} = '.format(num1, num2))
    print(num1 * num2)
  elif method == 'div':  
    print('{} / {} = '.format(num1, num2))
    print(num1 / num2)
  else:
    print('Pls choose a valid method add, sub, mult or div')

calculate()

