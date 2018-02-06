# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.

arith_meth = input("What method of arithmetic would you like to use? add, sub, mult, or div?")

num1 = input("What's your first integer?")
num1 = int(num1)
num2 = input('and your second integer?')
num2 = int(num2)

if arith_meth == 'add':
  answer = num1 + num2
elif arith_meth == 'sub':
  answer = num1 - num2
elif arith_meth == 'mult':
  answer = num1 * num2
elif arith_meth == 'div':
  answer = num1 / num2
else:
  print('you must put the arithmetic method as printed')

print(answer)
