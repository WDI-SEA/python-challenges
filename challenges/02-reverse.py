# Python offers several ways to reverse a String. This is a classic thing
# that lots of people want to do. It's probably easy to look up this
# answer on Stack Overflow.
#
# This website of 30 Python Tips and Tricks also happens to point out
# several ways to reverse a string, and it's a good read!
#
# http://www.techbeamers.com/essential-python-tips-tricks-programmers/?utm_source=mybridge&utm_medium=blog&utm_campaign=read_more#tip1

string_input = input('Please input a word, phrase, or sentence here ')

print(string_input)

def reverse_string (string):
    rev_string_list = []
    split_string = string.split()
    print(split_string)
    for i in range(len(split_string)):
        split_string.pop(i)

        return(rev_string_list)

print(reverse_string(string_input))