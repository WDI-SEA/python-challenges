# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.

num1 = float(input('enter a number: '))
operator = input('enter operator: ')
num2 = float(input('enter another number: '))

if operator == "+":
  print(num1 + num2)
elif operator == "-":
  print(num1 - num2)
elif operator == "*" or "x":
  print(num1 * num2)
elif operator == "/":
  print(num1 / num2)
elif operator == "%":
  print(num1 % num2)
