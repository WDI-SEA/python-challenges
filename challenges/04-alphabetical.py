# You'll need to use a couple of built in functions to alphabetize a string.
# Try to avoid looking up the exact answer and look at built in functions for
# lists and strings instead.

str = input('Initial String: ')

list = list(str)
list.sort()

sorted_string = ''.join(list)

print(sorted_string)
