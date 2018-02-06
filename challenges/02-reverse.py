# Python offers several ways to reverse a String. This is a classic thing
# that lots of people want to do. It's probably easy to look up this
# answer on Stack Overflow.
#
# This website of 30 Python Tips and Tricks also happens to point out
# several ways to reverse a string, and it's a good read!
#
# http://www.techbeamers.com/essential-python-tips-tricks-programmers/?utm_source=mybridge&utm_medium=blog&utm_campaign=read_more#tip1

my_string = input('Please enter a string: ')

my_string_arr = list(my_string)
my_string_arr.reverse()
my_string_str = ''.join(my_string_arr)

print('Here is the reversed string: {0}'.format(my_string[::-1]))
print('Here is another way :{0}'.format(my_string_str))