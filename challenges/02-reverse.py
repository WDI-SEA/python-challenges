# Python offers several ways to reverse a String. This is a classic thing
# that lots of people want to do. It's probably easy to look up this
# answer on Stack Overflow.
#
# This website of 30 Python Tips and Tricks also happens to point out
# several ways to reverse a string, and it's a good read!
#
# http://www.techbeamers.com/essential-python-tips-tricks-programmers/?utm_source=mybridge&utm_medium=blog&utm_campaign=read_more#tip1

# def reverseString(str):
#     reversed = ""
#     for i in range(1,len(str)+1):
#         print(str[-i], f'this letter at index -{i}')
#         reversed += str[-i]
#     return reversed

def reverseString(str): 
    reverse = ''
    for letter in str: 
        reverse = letter + reverse
    return reverse

print(reverseString('hello world'))

