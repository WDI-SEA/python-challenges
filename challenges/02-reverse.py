# Python offers several ways to reverse a String. This is a classic thing
# that lots of people want to do. It's probably easy to look up this
# answer on Stack Overflow.
#
# This website of 30 Python Tips and Tricks also happens to point out
# several ways to reverse a string, and it's a good read!
#
# http://www.techbeamers.com/essential-python-tips-tricks-programmers/?utm_source=mybridge&utm_medium=blog&utm_campaign=read_more#tip1

# def reversed_str(str):
#     list_of_str=[]
#     for char in str:
#         list_of_str.append(char)
#     for char in reversed(list_of_str):
#         print(char)

# reversed_str("apple")

def reverse_string(string):  
    str1 = ""    
    for i in string:  
        str1 = i + str1  
    return str1 
string="apple"

print(reverse_string(string))