# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.

def calculator():
	operation = input ("What calculation would you like to do? (add, sub, mult, div) \n")
	number_1 = int(input('enter your number 1 \n'))
	number_2 = int(input('enter your number 2 \n'))

	if operation  == 'add':
		print('{} + {} = '.format(number_1, number_2))
		print(number_1 + number_2)
	elif operation == 'sub':
		print('{} - {} = '.format(number_1, number_2))
		print(number_1 - number_2)
	elif operation == 'mult':
		print('{} * {} = '.format(number_1, number_2))
		print(number_1 * number_2)
	elif operation == 'div':
		print('{} / {} = '.format(number_1, number_2))
		print(number_1 / number_2)
	else:
		print ('You must enter a valid input')


calculator()