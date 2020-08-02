# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.

calc = input("Which calculation would you like to perform? (add, sub, mult, div) ").lower()
num1 = int(input("What is number 1? "))
num2 = int(input("What is number 2? "))

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
  print("Please enter a valid calculation to perform.")