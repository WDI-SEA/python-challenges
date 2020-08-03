# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.

def add(x, y):
  return x + y

def sub(x, y):
  return  x - y

def mult(x, y):
  return x * y

def div(x, y):
  return x / y

def gather_input():
  problemType = input("What type of calc would you like to do? (add, sub, mult, div)")
  if problemType in ('add', 'sub', 'mult', 'div'):
    number1 = int(input("What is number 1?"))
    number2 = int(input("What is number 2?"))

    if problemType == 'add':
      print("Your result is ", add(number1, number2))

    elif problemType == 'sub':
      print("Your result is ", sub(number1, number2))

    elif problemType == 'mult':
      print("Your result is ", mult(number1, number2))

    elif problemType == 'div':
      print("Your result is ", div(number1, number2))
  
  else:
  print("Invalid Input")

gather_input()

#YAY IT WORKS!!

# Thanks for the help: https://www.programiz.com/python-programming/examples/calculator
