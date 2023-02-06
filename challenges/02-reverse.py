# Python offers several ways to reverse a String. This is a classic thing
# that lots of people want to do. It's probably easy to look up this
# answer on Stack Overflow.
#
# This website of 30 Python Tips and Tricks also happens to point out
# several ways to reverse a string, and it's a good read!
#
# http://www.techbeamers.com/essential-python-tips-tricks-programmers/?utm_source=mybridge&utm_medium=blog&utm_campaign=read_more#tip1

# # the forbidden easy way
# string = "Reverse me" [::-1]
# print(str(string))


def inverse(str):
    reversed_string = ''
    for i in range(len(str) - 1, -1, -1):
        reversed_string += str[i]
    return reversed_string 
    
string_input = input("Enter a string: ")
print(inverse(string_input))