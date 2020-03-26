# Python offers several ways to reverse a String. This is a classic thing
# that lots of people want to do. It's probably easy to look up this
# answer on Stack Overflow.
#
# This website of 30 Python Tips and Tricks also happens to point out
# several ways to reverse a string, and it's a good read!
#
# http://www.techbeamers.com/essential-python-tips-tricks-programmers/?utm_source=mybridge&utm_medium=blog&utm_campaign=read_more#tip1

def reverse(working_string):
    return_string = ''
    string_length = len(working_string)
    for index in range(0, string_length):
        return_string += working_string[string_length - index - 1]
    return return_string

user_input = input("Enter a string ")

# print(user_input[::-1])
print(reverse(user_input))