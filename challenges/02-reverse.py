# Python offers several ways to reverse a String. This is a classic thing
# that lots of people want to do. It's probably easy to look up this
# answer on Stack Overflow.
#
# This website of 30 Python Tips and Tricks also happens to point out
# several ways to reverse a string, and it's a good read!
#
# http://www.techbeamers.com/essential-python-tips-tricks-programmers/?utm_source=mybridge&utm_medium=blog&utm_campaign=read_more#tip1



#prompt the user to inter something
string = input(" Enter the string to reverse")
#initiliazing empty string
reversed_string = ""

for i in range(len(string)):
    reversed_string += string[len(string)-i-1]
# The expression 'string[len(string)-i-1]' 
# calculates the index of the character to be added to the 
# 'reversed_string' variable.

# The loop continues until all the characters in the input string have been added to the 
# 'reversed_string' variable.
print(reversed_string)
