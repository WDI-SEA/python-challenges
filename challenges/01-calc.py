# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.

add = 'add'
sub = 'sub'
multi = 'multi'
div = 'div'


op = input('Enter a op')
print(op)
num1 = int(input('what is number 1'))
print(num1)
num2 = int(input('what is number 2'))
print(num2)
if op == add:
    print(num1 + num2)
if op == sub:
    print(num1 - num2)
if op == multi:
    print(num1 * num2)
if op == div:
    print(num1 / num2)



