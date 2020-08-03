# Python offers several ways to reverse a String. This is a classic thing
# that lots of people want to do. It's probably easy to look up this
# answer on Stack Overflow.
#
# This website of 30 Python Tips and Tricks also happens to point out
# several ways to reverse a string, and it's a good read!
#
# http://www.techbeamers.com/essential-python-tips-tricks-programmers/?utm_source=mybridge&utm_medium=blog&utm_campaign=read_more#tip1


some_string = "oo bla di oo bla da"
print(f"Original string: {some_string}")

def reverse_string():
  rev_str = ""
  index = len(some_string)
  
  while index > 0:
    rev_str += some_string[index - 1]
    index -= 1
  print(f"Reversed string: {rev_str}")

reverse_string()