# Python offers several ways to reverse a String. This is a classic thing
# that lots of people want to do. It's probably easy to look up this
# answer on Stack Overflow.
#
# This website of 30 Python Tips and Tricks also happens to point out
# several ways to reverse a string, and it's a good read!
#
# http://www.techbeamers.com/essential-python-tips-tricks-programmers/?utm_source=mybridge&utm_medium=blog&utm_campaign=read_more#tip1

str = 'reverse_me'
string = "".join(reversed(str))
print(string)

def reversedString(str):
    reversed = ''
    for i in range(1, len(str) + 1):
        reversed += str[-i]
    return reversed

print(reversedString(str))

def reversedString_two(str):
    reversed = ''
    for letter in str:
        reversed = letter + reversed
    return reversed

print(reversedString_two(str))