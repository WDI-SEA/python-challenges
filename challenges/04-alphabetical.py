# You'll need to use a couple of built in functions to alphabetize a string.
# Try to avoid looking up the exact answer and look at built in functions for
# lists and strings instead.
string = input('Give me a string to sort the alphabet')
the_list = list(string)
the_list.sort()

alphabet = ''
for char in the_list:
    alphabet += char

print(alphabet)
