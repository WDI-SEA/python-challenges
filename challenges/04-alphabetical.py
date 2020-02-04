# You'll need to use a couple of built in functions to alphabetize a string. 
# Try to avoid looking up the exact answer and look at built in functions for
# lists and strings instead.

string = input('Give me a string to alphabetize')

new_list = list(string)

new_list.sort()

new_string = ''

print(new_string.join(new_list))