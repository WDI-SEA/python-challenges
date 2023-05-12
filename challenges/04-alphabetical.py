# You'll need to use a couple of built in functions to alphabetize a string. 
# Try to avoid looking up the exact answer and look at built in functions for
# lists and strings instead.

def sort_string(string):
    sorted_string = ''.join(sorted(string))
    return sorted_string

user_string = input("Give me a string\n")

print(sort_string(user_string))
