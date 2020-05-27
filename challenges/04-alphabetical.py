# You'll need to use a couple of built in functions to alphabetize a string. 
# Try to avoid looking up the exact answer and look at built in functions for
# lists and strings instead.

string = input('Need something in alphabetical order? Put it here! ')

def alphabetize(string):
    print('Here ya go, m8!')
    print('Original String: ' + string)
    print('Alphabetized string: '+''.join(sorted(string)))
alphabetize(string)

