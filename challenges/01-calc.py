# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.

ask = input('What calculation would you like to do? (add, sub, mult, div) \n')
first = int(input('enter first num\n'))
second = int(input('enter second num\n'))

if ask=='add':
    result = first + second
elif ask=='sub':
    result = first-second
elif ask =='mult':
    result = first * second
elif ask == "div":
    result = first / second
else: 
    result="put the right params"
print(f'your result is: {result}')