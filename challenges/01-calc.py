# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.

num1 = None
num2 = None

print('Enter first number')
num1 = int(input())
print('Enter second number')
num2 = int(input())

print('Sum is...')
print(num1 + num2)