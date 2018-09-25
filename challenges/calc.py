operator = input("What calculation would you like to do? (add, sub, mult, div)")

while operator not in ["add", "sub", "mult", "div"]:
	print("bad input:", operator)
	operator = input("Try Again! Pick one of these: (add, sub, mult, div)")

num1 = None
num2 = None

while not isinstance(num1, int):
	try:
		num1 = int(input("What is your first number?"))
	except:
		print("That is not a number!")

while not isinstance(num2, int):
	try:
		num2 = int(input("What is your second number?"))
	except:
		print("That is not a number!")

if operator == "add":
	print(num1, "plus", num2, "is", num1 + num2)
elif operator == "sub":
	print(num1, "minus", num2, "is", num1 - num2)
elif operator == "mult":
	print(num1, "times", num2, "is", num1 * num2)
elif operator == "div":
	print(num1, "divided by", num2, "is", num1 / num2)

print("thanks")