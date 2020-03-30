# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.


operator = input('What do you wanna do?')
num1 = int(input('first number go here\n'))
num2 = int(input('secondd number go here\n'))
result = 'bad operator'

if operator == 'add':
    result = num1 + num2
elif operator == 'sub':
    result = num1 - num2
elif operator == 'multi':
    result = num1 * num2
elif operator == 'div':
    result - num1 / num2
print(f'Your result was ' {result}) 