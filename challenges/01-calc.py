# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.

# What calculation would you like to do? (add, sub, mult, div)
calc = input('what calculation would you like to do?(add,sub,mult,div)')
num1 = int(input('what is number 1? '))
num2 = int(input('what is number 2? '))
result = ''

if calc == 'add':
  result = num1 + num2
elif calc == 'sub':
  result = num1 - num2
elif calc == 'mult':
  result = num1 * num2
elif calc == 'div':
  result = num1 / num2
else : result = 'wont work because...invalid operator'
# add
# What is number 1?
# 3
# What is number 2?
# 6
# Your result is 9

print(f'your result is {result}')