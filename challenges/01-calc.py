# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.


math_method = input("What calculation would you like to do? (add, sub, mult, div)")
first_number = int(input("What is the first number?"))
second_number = int(input("What is the second number?"))

if(math_method == "add"):
	total_number = first_number + second_number
elif(math_method == "sub"):
	total_number = first_number - second_number
elif(math_method == "mult"):
	total_number = first_number * second_number
elif(math_method == "div"):
	total_number = first_number / second_number
else:
	total_number = "Invalid math method"

print(total_number)