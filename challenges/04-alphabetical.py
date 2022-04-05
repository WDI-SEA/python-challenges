# You'll need to use a couple of built in functions to alphabetize a string. 
# Try to avoid looking up the exact answer and look at built in functions for
# lists and strings instead.

string = input('Give me a string to alphabetize\n')
listed_string = list(string)
listed_string.sort()

alphabet = ''
for letter in listed_string:
    alphabet += letter

print(alphabet)