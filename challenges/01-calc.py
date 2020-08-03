# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.
print('Please enter first number: ')
a = input()

print('Please enter a second number: ')
b = input()

print('Please enter a mode (add, sub, mul, div): ')
mode = input()

if mode == 'add':
    print(int(a) + int(b))

elif mode == 'sub':
    print(int(a)-int(b))

elif mode == 'mul':
    print(int(a) * int(b))

elif mode == 'div':
    print(int(a) / int(b))

else:
    print(f'error parsing input {mode} , please try again')

