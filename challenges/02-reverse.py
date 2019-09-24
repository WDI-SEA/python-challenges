# Python offers several ways to reverse a String. This is a classic thing
# that lots of people want to do. It's probably easy to look up this
# answer on Stack Overflow.
#
# This website of 30 Python Tips and Tricks also happens to point out
# several ways to reverse a string, and it's a good read!
#
# http://www.techbeamers.com/essential-python-tips-tricks-programmers/?utm_source=mybridge&utm_medium=blog&utm_campaign=read_more#tip1

word = input("What word would you like to reverse? ")

def reverse(string):
    # print(string[-2])
    temp = []
    for i in range(1,len(string)+1):
        temp.append(string[-i])
    print("".join(temp))


reverse(word)