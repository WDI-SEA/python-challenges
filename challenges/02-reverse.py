# Python offers several ways to reverse a String. This is a classic thing
# that lots of people want to do. It's probably easy to look up this
# answer on Stack Overflow.
#
# This website of 30 Python Tips and Tricks also happens to point out
# several ways to reverse a string, and it's a good read!
#
# http://www.techbeamers.com/essential-python-tips-tricks-programmers/?utm_source=mybridge&utm_medium=blog&utm_campaign=read_more#tip1

# Option 1
# def reverse_string():
# 	string = input("Enter a string you would like to reverse: ")

# 	print(string[::-1]) # Backwards


# Option 2
# def reverse_string():
# 	string = input("Enter a string you would like to reverse: ")
# 	for x in reversed(string):  
#   		print( x, end = "" ) # end="" python 3 way to not create a new line at end of each print


# Option 3
# def reverse_string():
# 	string = input("Enter a string you would like to reverse: ")
# 	reversed_string = ''
# 	for letter in string:
# 		reversed_string = letter+reversed_string

# 	print(reversed_string)

# Option 4
def reverse_string():
	string = input("Enter a string you would like to reverse: ")

	# print(string[len(string):-len(string)-1:-1])
	# print(string[:-len(string)-1:-1])
	print(string[len(string)::-1])


reverse_string()
