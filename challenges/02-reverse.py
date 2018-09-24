# Python offers several ways to reverse a String. This is a classic thing
# that lots of people want to do. It's probably easy to look up this
# answer on Stack Overflow.
#
# This website of 30 Python Tips and Tricks also happens to point out
# several ways to reverse a string, and it's a good read!
#
# http://www.techbeamers.com/essential-python-tips-tricks-programmers/?utm_source=mybridge&utm_medium=blog&utm_campaign=read_more#tip1
def string_reverse(str1):

	rstr1 = ''
	index = len(str1)
	while index > 0:
		rstr1 += str1[ index -1 ]
		index = index - 1
	return rstr1
print(string_reverse('1234abcd'))