# Python offers several ways to reverse a String. This is a classic thing
# that lots of people want to do. It's probably easy to look up this
# answer on Stack Overflow.
#
# This website of 30 Python Tips and Tricks also happens to point out
# several ways to reverse a string, and it's a good read!
#
# http://www.techbeamers.com/essential-python-tips-tricks-programmers/?utm_source=mybridge&utm_medium=blog&utm_campaign=read_more#tip1

def reverse(string):
    temp = list(string)
    i = len(temp) - 1
    k = 0
    reverse = ['']
    # global x # using global
    x = ''
    while i >= 0:
        reverse.insert(k, temp[i])
        i-=1
        k+=1
        x = ''.join(reverse)
    return x 
    


print(reverse('chicken'))