# You'll need to use a couple of built in functions to alphabetize a string. 
# Try to avoid looking up the exact answer and look at built in functions for
# lists and strings instead.

# print(dir(list))
# print(dir(str))

string = input('Please enter a string to sort in alphabetic order!: \n')
print(string)
alphabetic = sorted(string.lower())
# print(alphabetic)
str = ''
print(str .join(alphabetic))