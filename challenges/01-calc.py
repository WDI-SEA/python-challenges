# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.


print('What calculation would you like to do? add, sub, mult, div')
math = input()

print('Please enter first number')
num_one = input()

print('Please enter second number')
num_two = input()

if math == 'add':
    print(int(num_one) + int(num_two))
elif math == 'sub':
    print(int(num_one) - int(num_two))
elif math == 'mult':
    print(int(num_one) * int(num_two))
elif math == 'div':
    print(int(num_one) / int(num_two))
else:
    print('Sorry, invalid input option, please try again')



