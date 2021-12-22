# Python offers several ways to reverse a String. This is a classic thing
# that lots of people want to do. It's probably easy to look up this
# answer on Stack Overflow.
#
# This website of 30 Python Tips and Tricks also happens to point out
# several ways to reverse a string, and it's a good read!
#
# http://www.techbeamers.com/essential-python-tips-tricks-programmers/?utm_source=mybridge&utm_medium=blog&utm_campaign=read_more#tip1

string = "Hello"
new_string = []

def reverse_string(string):
    string = list(string)
    print(string)
    print(len(string))
    for char in range(0, len(string)):
        new_string.append(string.pop())
        print(new_string)


reverse_string(string)
new_string = "".join(new_string)

print(new_string)

