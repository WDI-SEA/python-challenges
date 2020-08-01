# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.

def calculator():
  method = input("What method would you like to use?\n")

  x = int(input("What is the first number?\n"))
  y = int(input("What is the second number?\n"))

  if method == "addition":
    answer = x + y 
  elif method == "subtraction":
    answer = x - y
  elif method == "division":
    answer = x / y
  elif method == "multiply":
    answer = x * y 
  else: 
    ()
  
  print(f"The answer is {answer}")

calculator()