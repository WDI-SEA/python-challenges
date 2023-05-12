# You'll need to use a couple of built in functions to alphabetize a string. 
# Try to avoid looking up the exact answer and look at built in functions for
# lists and strings instead.

def alphabetize(string):
    sorted_string = ''.join(sorted(string))
    return sorted_string

input_string = input("Give me a string to alphabetize\n")
print('Alphabetized:', alphabetize(input_string))