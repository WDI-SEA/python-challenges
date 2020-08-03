# Python offers several ways to reverse a String. This is a classic thing
# that lots of people want to do. It's probably easy to look up this
# answer on Stack Overflow.
#
# This website of 30 Python Tips and Tricks also happens to point out
# several ways to reverse a string, and it's a good read!
#
# http://www.techbeamers.com/essential-python-tips-tricks-programmers/?utm_source=mybridge&utm_medium=blog&utm_campaign=read_more#tip1

string = input("Type whatever you want and I will make it look like David Lynch got his hands on it!")

# write a loop to reverse
def reversed(s):
  if len(s) == 0:
    return s
  else:
    return reversed(s[1:]) + s[0]

s = string
print (s)
print (reversed(s))