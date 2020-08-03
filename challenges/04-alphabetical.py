# You'll need to use a couple of built in functions to alphabetize a string. 
# Try to avoid looking up the exact answer and look at built in functions for
# lists and strings instead.
from itertools import accumulate
def sortString(str):
    return tuple(accumulate(sorted(str)))[-1]

str = 'WILD WILD WEST'
print(sortString(str))

# https://www.geeksforgeeks.org/python-ways-to-sort-letters-of-string-alphabetically/