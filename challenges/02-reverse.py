# Python offers several ways to reverse a String. This is a classic thing
# that lots of people want to do. It's probably easy to look up this
# answer on Stack Overflow.
#
# This website of 30 Python Tips and Tricks also happens to point out
# several ways to reverse a string, and it's a good read!
#
# http://www.techbeamers.com/essential-python-tips-tricks-programmers/?utm_source=mybridge&utm_medium=blog&utm_campaign=read_more#tip1

text = input("Enter a string to reverse: ")
# print('text:', text)
# char_list = [char for char in text]
# print(char_list)
# for i in text:
#     print("list start: ", char_list)
#     mover = 
#     char_list = char_list.insert(0, mover)
#     print("updated list", char_list)
# answer = "".join(char_list)

# print(answer)

def reverse(string):
    reversed_string = ""
    for i in string:
        reversed_string = i+reversed_string
    print("reversed string is:", reversed_string)

reverse(text)