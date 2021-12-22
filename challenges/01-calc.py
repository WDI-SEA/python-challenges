# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.


str = input('What calculation would you like to do? (add, sub, mult, div)  ')
# print('str:',str)
num1 = int(input('What is number 1?  '))
num2 = int(input('What is number 2?  '))
if str == 'add':
  print('Your result is',num1 + num2)
elif str == 'sub':
  print('Your result is',num1 - num2)
elif str == 'mult':
  print('Your result is',num1 * num2)
elif str == 'div':
  print('Your result is',num1 / num2)
else:
  print('not an option')