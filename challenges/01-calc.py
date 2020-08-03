# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.

calc = input('What calculation would you like to do? (add, sub, mult, div)').lower()
num1 = int(input("1st Number?"))
num2 = int(input("2nd Number?"))

if calc == "add":
  result = num1 + num2
  print(f"{num1} + {num2} = {result}")
elif calc == "sub":
  result = num1 - num2
  print(f"{num1} - {num2} = {result}")
elif calc == "mult":
  result = num1 * num2
  print(f"{num1} * {num2} = {result}")
elif calc == "div":
  result = num1 / num2
  print(f"{num1} / {num2} = {result}")
else:
  print("Please input a proper calculation.")