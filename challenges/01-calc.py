# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.

def getNum(prompt):
	try:
		num = int(input(prompt))
	except:
		print('This calculator only takes integers!')
		num = getNum(prompt)
	return num

def calculator():
	method = input("What calculation would you like to do? (add, sub, mult, div)\n")
	validMethods = ['add', 'sub', 'mult', 'div']
	if method.lower() in validMethods:
		num1 = getNum("Enter the first number:\n")
		num2 = getNum("Enter the second number:\n")
		if method.lower() == 'add':
			return num1+num2
		elif method.lower() == 'sub':
			return num1-num2
		elif method.lower() == 'mult':
			return num1*num2
		else:
			return num1/num2
	else:
		print(method+" is an invalid operation!")
		calculator();

print(calculator())

# What calculation would you like to do? (add, sub, mult, div)
# add
# What is number 1?
# 3
# What is number 2?
# 6
# Your result is 9