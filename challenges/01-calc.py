# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.
operation = input("What operation would you like to perform? (add, sub, mult, div)")
if operation == "add":
  num1 = input("What is number 1?")
  num2 = input("What is number 2?")
  result = num1 + num2
elif operation == "sub":
  num1 = input("What is number 1?")
  num2 = input("What is number 2?")
  result = num1 - num2
elif operation == "mult":
  num1 = input("What is number 1?")
  num2 = input("What is number 2?")
  result = num1 * num2
elif operation == "div":
  num1 = input("What is number 1?")
  num2 = input("What is number 2?")
  result = num1 / num2
else:
  print("Invalid operation type. Please try again")
if result:
  print(f'Your result is {result}.')