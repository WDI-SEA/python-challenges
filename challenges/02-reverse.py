# Python offers several ways to reverse a String. This is a classic thing
# that lots of people want to do. It's probably easy to look up this
# answer on Stack Overflow.
#
# This website of 30 Python Tips and Tricks also happens to point out
# several ways to reverse a string, and it's a good read!
#
# http://www.techbeamers.com/essential-python-tips-tricks-programmers/?utm_source=mybridge&utm_medium=blog&utm_campaign=read_more#tip1
string = "banana"
reversed_string = string[::-1]
print (reversed_string)

string="cucumber"
reversed_string = "".join(reversed(string))
print(reversed_string)

string= "hello world"
reversed_string = ""
for char in string:
    reversed_string = char + reversed_string
print(reversed_string)