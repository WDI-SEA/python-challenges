# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.
def calculator():
  # get all user input
  method = input("What method would you like to use?\n")
  
  # get numbers from user
  x = int(input("What is number 1?\n"))
  y = int(input("What is number 1?\n"))

  methods = {
    "add": x + y,
    "multiply": x * y,
    "div": x / y,
    "sub": x - y,
  }

  if (method in methods):
    return methods[method]
  else:
    return print("Argh - you did not give a correct method! Try again.")


print(calculator())