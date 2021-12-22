# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.

question = input("What calculation would you like to do? (add, sub, mult, div)")
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if question == 'add':
  print(num1 + num2)

elif question == 'sub':
  print(num1 - num2)

elif question == 'mult':
  print(num1 * num2)

elif question == 'div':
  print(num1 / num2)

