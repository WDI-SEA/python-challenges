# Python offers several ways to reverse a String. This is a classic thing
# that lots of people want to do. It's probably easy to look up this
# answer on Stack Overflow.
#
# This website of 30 Python Tips and Tricks also happens to point out
# several ways to reverse a string, and it's a good read!
#
# http://www.techbeamers.com/essential-python-tips-tricks-programmers/?utm_source=mybridge&utm_medium=blog&utm_campaign=read_more#tip1

word = input("Enter a word to reverse: ")

def reverse_word(word):
    drow = ""
    for letter in reversed(word):
        drow += letter
    print(drow)
    print("".join(reversed(word)))

reverse_word(word)

# python slice syntax (works on lists or strings)
my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# [slice start (default 0): slice end (default end of list): step (default 1)]
my_list_copy = my_list[::] # make a copy with defaults
print(my_list[::-1])

print(word[::-1])