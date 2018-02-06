# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.
print('What calculation would you like to do? (add, sub, mult, div)')
operator = input()
print('What is number 1?')
num1 = input()
print('What is number 2?')
num2 = input()

if(operator == 'add'):
  result = int(num1) + int(num2)
elif(operator == 'sub'):
  result = int(num1) - int(num2)
elif(operator == 'mult'):
  result = int(num1) * int(num2)
elif(operator == 'div'):
  result = int(num1) / int(num2)
else:
  result = 'N/A'

print('Your result is ', result)