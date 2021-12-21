# You'll need to use a couple of built in functions to alphabetize a string. 
# Try to avoid looking up the exact answer and look at built in functions for
# lists and strings instead.

def sort_string(string):
    list_string = sorted(string)
    sorted_string = ''.join(list_string)
    print(sorted_string)
sort_string('hello')