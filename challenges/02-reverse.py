# Python offers several ways to reverse a String. This is a classic thing
# that lots of people want to do. It's probably easy to look up this
# answer on Stack Overflow.
#
# This website of 30 Python Tips and Tricks also happens to point out
# several ways to reverse a string, and it's a good read!
#
# http://www.techbeamers.com/essential-python-tips-tricks-programmers/?utm_source=mybridge&utm_medium=blog&utm_campaign=read_more#tip1

"I hope this works"[::-1]
string = input("Type words here:")
def reverseIt(string):
  reverse = ''
  for letter in string:
    reverse = letter + reverse
  return reverse
  print(reverseIt(string))

reverseIt()

# IT WORKS YAYYY!!!


# THANKS FOR THE HELP: https://www.journaldev.com/23647/python-reverse-string