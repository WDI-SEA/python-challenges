# Python offers several ways to reverse a String. This is a classic thing
# that lots of people want to do. It's probably easy to look up this
# answer on Stack Overflow.
#
# This website of 30 Python Tips and Tricks also happens to point out
# several ways to reverse a string, and it's a good read!
#
# http://www.techbeamers.com/essential-python-tips-tricks-programmers/?utm_source=mybridge&utm_medium=blog&utm_campaign=read_more#tip1

# n = 0
# while n < 10:
#   n++
#
#
# for i in range(0, 10):
#   if i % 2 == 0:
#     print("{} is even".format(i))
#   if i % 2 == 1:
#     print("{} is odd".format(i))



straight = input('Enter something to reverse')
reversed = ''

n = -1
while n < len(straight):
  reversed = + straight[n]
  n = n - 1
