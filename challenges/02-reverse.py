# Python offers several ways to reverse a String. This is a classic thing
# that lots of people want to do. It's probably easy to look up this
# answer on Stack Overflow.
#
# This website of 30 Python Tips and Tricks also happens to point out
# several ways to reverse a string, and it's a good read!
#
# http://www.techbeamers.com/essential-python-tips-tricks-programmers/?utm_source=mybridge&utm_medium=blog&utm_campaign=read_more#tip1

string = input('Enter a string:')
# reverse_list = None
# for i,char in enumerate(reversed(string)):
#     print(char)

def reverse_string(string):
    new_string = ''
    index = len(string)
    while index:
        index -=1
        new_string += string[index]
    return new_string

print(reverse_string(string))

