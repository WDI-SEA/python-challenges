# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.

operator = input('what calculation would you like to do? (add, sub, mult, div)\n')

num1 = input('What is number 1?\n')

num2 = input('What is number 2?\n')

# result = 0

if(operator=="add"):
    result = int(num1)+int(num2)
if(operator=="sub"):
    result = int(num1)-int(num2)
if(operator=="mult"):
    result = int(num1)*int(num2)
if(operator=="div"):
    result = int(num1)/int(num2)

print(f'your result is {result}')