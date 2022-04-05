# Python offers several ways to reverse a String. This is a classic thing
# that lots of people want to do. It's probably easy to look up this
# answer on Stack Overflow.
#
# This website of 30 Python Tips and Tricks also happens to point out
# several ways to reverse a string, and it's a good read!
#
# http://www.techbeamers.com/essential-python-tips-tricks-programmers/?utm_source=mybridge&utm_medium=blog&utm_campaign=read_more#tip1

def reverse(str):
    i = 0
    strList = list(str)
    while i < len(str)/2:
        char = strList[i]
        strList[i] = strList[len(str) - 1 - i]
        strList[len(str) - 1 - i] = char
        i += 1
    print("".join(strList))
