# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.
def calculator():
	method = input("what calculation would you like to do?(add, subtract, multiply, divide): " )
	num1 = int(input("first number?: "))
	num2 = int(input("second number?: "))

	if method == "add":
		print("the result of {} + {} is {}".format(num1, num2, (num1+num2)))
	elif method == "subtract":
		print("the result of {} - {} is {}".format(num1, num2, (num1-num2)))
	elif method == "multiply":
		print("the result of {} * {} is {}".format(num1, num2, (num1*num2)))
	elif method == "divide":
		print("the result of {0} / {1} is {2}".format(num1, num2, (num1/num2)))
	else:
		print("not a valid method entry")

calculator()
