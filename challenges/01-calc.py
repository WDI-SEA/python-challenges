# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.


# prompt = '>'
# print('What calculation would you like to do? (add, sub, mult, div)')
# method = input(prompt)
method = input('What calculation would you like to do? (add, sub, mult, div)')
# print('What is number 1?')
# num1 = input(prompt)
num1 = input('What is number 1?')
# print('What is number 2?')
# num2 = input(prompt)
num2 = input('What is number 2?')
if method == 'add':
    result = int(num1) + int(num2)
    print('Your result is ' + str(result))
elif method == 'sub':
    result = int(num1) - int(num2)
    print('Your result is ' + str(result))
elif method == 'mult':
    result = int(num1) * int(num2)
    print('Your result is ' + str(result))
else:
    result = int(num1) / int(num2)
    print('Your result is ' + str(result))