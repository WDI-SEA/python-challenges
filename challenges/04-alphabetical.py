# You'll need to use a couple of built in functions to alphabetize a string. 
# Try to avoid looking up the exact answer and look at built in functions for
# lists and strings instead.

# str = "string"
# arr = list(str)
# arr.sort()
# print(arr)

# str = "this is a bunch of strings"
# arr = str.split()
# arr.sort()
# print(arr)

def alphabetize(string):
    string = input('give me a string to alphabetize')
    arr = list(string)
    arr.sort()
    return ''.join(arr)

print(alphabetize('word'))
