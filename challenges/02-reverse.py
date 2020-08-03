# Python offers several ways to reverse a String. This is a classic thing
# that lots of people want to do. It's probably easy to look up this
# answer on Stack Overflow.
# This website of 30 Python Tips and Tricks also happens to point out
# several ways to reverse a string, and it's a good read!
# http://www.techbeamers.com/essential-python-tips-tricks-programmers/?utm_source=mybridge&utm_medium=blog&utm_campaign=read_more#tip1

print("Enter a string: ")
str = "reverse_me" # initial string
reversedString=[]
# index = len(str) # calculate length of string and save in index
# while index > 0: 
#     reversedString += str[ index - 1 ] # save the value of str[index-1] in reverseString
#     index = index - 1 # decrement index
reversedstring=''.join(reversed(str))
print(reversedString) # reversed stringc