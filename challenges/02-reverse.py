# Python offers several ways to reverse a String. This is a classic thing
# that lots of people want to do. It's probably easy to look up this
# answer on Stack Overflow.
#
# This website of 30 Python Tips and Tricks also happens to point out
# several ways to reverse a string, and it's a good read!
#


string = input("What would you like to reverse today: ")

def reverse_it(words):
  to_reverse = list(words)
  to_reverse.reverse()
  print(''.join(to_reverse))

reverse_it(string)