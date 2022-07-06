# Python offers several ways to reverse a String. This is a classic thing
# that lots of people want to do. It's probably easy to look up this
# answer on Stack Overflow.
#
# This website of 30 Python Tips and Tricks also happens to point out
# several ways to reverse a string, and it's a good read!
#
# http://www.techbeamers.com/essential-python-tips-tricks-programmers/?utm_source=mybridge&utm_medium=blog&utm_campaign=read_more#tip1

# print("Enter a string:")
# input_string = input()

# def reverse_string(input_string):   
#     input_string = "".join(reversed(input_string))
#     return input_string
# print(reverse_string(input_string))

def reverse_str(str):
    rev_word = ""
    for letter in str:
        rev_word = letter + rev_word
    return rev_word
word = input("Enter a string:\n")
print(reverse_str(word))