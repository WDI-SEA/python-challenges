# You'll need to use a couple of built in functions to alphabetize a string. 
# Try to avoid looking up the exact answer and look at built in functions for
# lists and strings instead.

def alphabetize(string):
    x = sorted(string)
    string = ''.join(x)
    print(string)


user_input = input('Input string to be alphabetized\n')
alphabetize(user_input)