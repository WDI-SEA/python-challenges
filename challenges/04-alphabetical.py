# You'll need to use a couple of built in functions to alphabetize a string. 
# Try to avoid looking up the exact answer and look at built in functions for
# lists and strings instead.


string = input('Give me a string to alphabetize\n')
string_list = sorted(string)

def alphabetize_string(string):
    return ''.join(sorted(string))
print(alphabetize_string(string))