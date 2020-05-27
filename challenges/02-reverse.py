# Python offers several ways to reverse a String. This is a classic thing
# that lots of people want to do. It's probably easy to look up this
# answer on Stack Overflow.
#
# This website of 30 Python Tips and Tricks also happens to point out
# several ways to reverse a string, and it's a good read!
#
# http://www.techbeamers.com/essential-python-tips-tricks-programmers/?utm_source=mybridge&utm_medium=blog&utm_campaign=read_more#tip1
def reverse(word): 
    result=''
    for i in word:
        result = i + result
    print(result)
reverse('banana')

def rev_string(str):
    result2=''
    for x in range(len(str), 0, -1):
        result2 += str[(x-1)]
    print(result2)

rev_string('tomato')

