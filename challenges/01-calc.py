# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.
calc = input("What calculation would you like to do? (add, sub, mult, div)")
v1 = int(input("What is your first number?"))
v2 = int(input("What is your second number?"))

def calculator(calc, v1, v2):
	if (calc == "add"):
		print("your result is", v1+v2)
	elif (calc == "sub"):
		print("your result is", v1-v2)
	elif (calc == "mult"):
		print("your result is", v1*v2)
	elif (calc == "div"):	
		print("your result is", v1/v2)
	else:
		print("sorry, try a different calc")
		calc = input("What calculation would you like to do? (add, sub, mult, div)")
				

calculator(calc, v1, v2)		
