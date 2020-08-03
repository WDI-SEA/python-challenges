# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.

#  testing
food = input("What do you want to eat?")
count = input(f"How many servings would you like?")

count = int(count)

for i in range(count):
  print(f"Here's another serving of {food}!")

# actual solution
calc = input("What calculation should I perform? add, subtract, multiply, divide")

num1 = input("What is the first number?")

num2 = input("What is the second number?")

plus = int(num1) + int(num2)

if calc == "add":
  print(plus)

minus = int(num1) - int(num2)

if calc == "subtract":
  print(minus)

multiply = int(num1) * int(num2)

if calc == "multiply":
  print(multiply)

divide = int(num1) / int(num2)

if calc == "divide":
  print(divide)


# in class solution, more object-oriented and elegant
def calculator():
  # declare a variable to store user input
  method = input("What method would you like to use?\n")

  # get number inputs from user 
  x = int(input("What is number one?\n"))
  y = int(input("What is number two?\n"))

  # most elegant way to do this
  # since python is object oriented
  methods = {
    "add": x + y,
    "subtract": x - y,
    "multiply": x * y,
    "divide": x / y
  }

  if (method in methods):
    return print(methods[method])
  else:
    return print("Not a valid method! Try again.")

calculator()
