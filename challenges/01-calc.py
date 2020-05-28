# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.

op = input('What calculation would you like to do? (add, sub, mult, div) ')
num1 = input('what is num 1? \n')
num2 = input('what is num 2? \n')
calc = 0

if op == 'add': 
    result = int(num1) + int(num2)
elif op == 'sub':
   result = int(num1) - int(num2)
elif op == 'mult':
   result = int(num1) * int(num2)
elif op == 'div':
   result = int(num1) // int(num2)
   
print("Your result is ", calc)

