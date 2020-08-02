# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.


operator = input('What calculation would you like to do ? ')
num1 = int(input('What is the first number ? '))
num2 = init(input('What is the second number ?'))
result = 'Bad operator ?'

if operator == 'add':
    result == num1 +num2

elif operator == 'sub':
   result = num1 -num2
elif operator == 'div':
    result = num1 /num2
elif operator == 'mult':
    result = num1 * num2

print(f' Your result was {result}!')



