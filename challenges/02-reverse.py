# Python offers several ways to reverse a String. This is a classic thing
# that lots of people want to do. It's probably easy to look up this
# answer on Stack Overflow.
#
# This website of 30 Python Tips and Tricks also happens to point out
# several ways to reverse a string, and it's a good read!
#
# http://www.techbeamers.com/essential-python-tips-tricks-programmers/?utm_source=mybridge&utm_medium=blog&utm_campaign=read_more#tip1

# create the variable with a text that will be reversed
normal_text = "reverse"

# variable to store the reversed text 
reversed_text = ""

# initialize index vairable to grab list length
index = len(normal_text)

# loop and print 
while index > 0:
    reversed_text += normal_text[index - 1]
    index = index -1
    print(reversed_text)