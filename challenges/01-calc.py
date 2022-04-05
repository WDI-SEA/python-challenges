# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.

method = input('select a method: (add, subtract, multiply,divide) ')
num1 = input('input a number: ')
num2 = input('input another number: ')
print(method, num1, num2)

if method == 'add':
    print(int(num1)+int(num2))
elif method=='subtract':
    print(int(num1)-int(num2))
elif method == 'multiply':
    print(int(num1)*int(num2))
elif method == 'divide':
    print(int(num1)/int(num2))
else: print('thats not a valid method')