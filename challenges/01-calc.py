# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.
def calculator():
	operation = input("What calculation would you like to do (add, sub, mult, div)\n")
	num1 = input("Enter first number\n")
	num2 = input("Enter second number\n")
	if(operation == 'add'):
		result = int(num1) + int(num2)
		result = str(result)
		print('Your result is ' + result)
	if(operation == 'sub'):
		result = int(num1) - int(num2)
		result = str(result)
		print('Your result is ' + result)
	if(operation == 'mult'):
		result = int(num1) * int(num2)
		result = str(result)
		print('Your result is ' + result)
	if(operation == 'div'):
		result = int(int(num1) / int(num2))
		result = str(result)
		print('Your result is ' + result)
calculator()