# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.

calc = input("What calculation would you like to do? (add, sub, mult, div)")
num1 = input("first number")
num2 = input("second number")
val1 = int(num1)
val2 = int(num2)
if(calc == 'add'):
	print(val1 + val2)
elif(calc == 'sub'):
	print(val1-val2)
elif(calc == 'mult'):
	print(val1*val2)
else: print(val1//val2)

