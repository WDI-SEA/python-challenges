# Python offers several ways to reverse a String. This is a classic thing
# that lots of people want to do. It's probably easy to look up this
# answer on Stack Overflow.
#
# This website of 30 Python Tips and Tricks also happens to point out
# several ways to reverse a string, and it's a good read!
#
# http://www.techbeamers.com/essential-python-tips-tricks-programmers/?utm_source=mybridge&utm_medium=blog&utm_campaign=read_more#tip1


string = "Hello, World!"
reversed_string = ""

for i in range(len(string) - 1, -1, -1):
    reversed_string += string[i]

print(reversed_string)

#  it uses a for loop to iterate over the range of indices of string in reverse order (len(string) - 1 to 0), incrementing by -1. On each iteration, it accesses the character at the current index of string and adds it to the end of reversed_string.

