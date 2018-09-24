# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.

operation = input("What calculation would you like to do? (add, sub, mult, div)\n")
num1 = int(input("What is number 1?\n"))
num2 = int(input("What is number 2?\n"))

if(operation == 'add'):
  print(num1 + num2)
elif(operation == 'sub'):
  print(num1 - num2)
elif(operation == 'mult'):
  print(num1 * num2)
elif(operation == 'div'):
  print(num1 / num2)
else:
  print('Invalid operation')