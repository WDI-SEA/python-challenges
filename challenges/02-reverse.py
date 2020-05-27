# Python offers several ways to reverse a String. This is a classic thing
# that lots of people want to do. It's probably easy to look up this
# answer on Stack Overflow.
#
# This website of 30 Python Tips and Tricks also happens to point out
# several ways to reverse a string, and it's a good read!
#
# http://www.techbeamers.com/essential-python-tips-tricks-programmers/?utm_source=mybridge&utm_medium=blog&utm_campaign=read_more#tip1

strn = input("what is the word you want to reverse? ")

def reversestr(strn):
    strn2 = ""
    for i in range(len(strn) -1, -1 , -1):
        strn2 = strn2 + strn[i]
    print(strn2)

reversestr(strn)