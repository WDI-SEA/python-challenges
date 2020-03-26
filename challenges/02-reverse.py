# Python offers several ways to reverse a String. This is a classic thing
# that lots of people want to do. It's probably easy to look up this
# answer on Stack Overflow.
#
# This website of 30 Python Tips and Tricks also happens to point out
# several ways to reverse a string, and it's a good read!
#
# http://www.techbeamers.com/essential-python-tips-tricks-programmers/?utm_source=mybridge&utm_medium=blog&utm_campaign=read_more#tip1
import math

def reverse_string(user_input):
  user_list = list(user_input)
  for i in range(math.ceil(len(user_list)/2)):
    user_list[i], user_list[-(i+1)] = user_list[-(i+1)], user_list[i]
  
  reversed = "".join(user_list)
  print(reversed)

user_input = input("Enter a string:")
reverse_string(user_input)