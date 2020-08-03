# Python offers several ways to reverse a String. This is a classic thing
# that lots of people want to do. It's probably easy to look up this
# answer on Stack Overflow.
#
# This website of 30 Python Tips and Tricks also happens to point out
# several ways to reverse a string, and it's a good read!
#
# http://www.techbeamers.com/essential-python-tips-tricks-programmers/?utm_source=mybridge&utm_medium=blog&utm_campaign=read_more#tip1

def string_reverser():
  print('Enter a string and behold as the mighty pyhton reverses it!')
  string = input('type your string here, human:')
  string = list(string)
  rev_string = ''
  for letter in reversed(string):
    rev_string += letter
    print(rev_string)

  print('Stand in Awe of the mighty python!')

string_reverser()