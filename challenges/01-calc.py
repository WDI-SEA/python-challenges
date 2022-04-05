# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.



operator = input("what operator would you like you use?")

number1 = input("what is the first number you would like to use?")
number2 = input("what is the second number you would like to use?")

if operator == "+":
    print(f'{int(number1)} + {int(number2)} = {int(number1) + int(number2)}')
if operator == "-":
      print(f'{int(number1)} - {int(number2)} = {int(number1) - int(number2)}')
if operator == "/":
      print(f'{int(number1)} / {int(number2)} = {int(number1) / int(number2)}')
if operator == "*":
      print(f'{int(number1)} * {int(number2)} = {int(number1) * int(number2)}')