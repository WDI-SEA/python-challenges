# You'll need to use a couple of built in functions to alphabetize a string. 
# Try to avoid looking up the exact answer and look at built in functions for
# lists and strings instead.

def alphabetize() :

    some_string = input('What would you like to alphabetize? ')

    to_list = list(some_string)

    to_list.sort()

    restringed = ''.join(to_list)

    print(restringed)

alphabetize()