# Python offers several ways to reverse a String. This is a classic thing
# that lots of people want to do. It's probably easy to look up this
# answer on Stack Overflow.
#
# This website of 30 Python Tips and Tricks also happens to point out
# several ways to reverse a string, and it's a good read!
#
# http://www.techbeamers.com/essential-python-tips-tricks-programmers/?utm_source=mybridge&utm_medium=blog&utm_campaign=read_more#tip1

def reverseString():
    reverse = []
    print('give us a string')
    # print(input()[::-1])
    for letter in input():
        reverse.append(letter)
    print(''.join(reversed(reverse)))
    
    

# reverseString()

# (lambda x, y: x + y)(2, 3)
# or 
# _(2, 3)

my_string = 'ldksfjlke kjekj fucucu elkrk'
blank_str = ''

for char in my_string:
    blank_str = char + blank_str

print(blank_str)
print(''.join(reversed(my_string)))

# doesnt work 
# print(reversed([1, 2, 3, 4]))
