# You'll need to use a couple of built in functions to alphabetize a string. 
# Try to avoid looking up the exact answer and look at built in functions for
# lists and strings instead.

def alpha(input):
    return str(sorted(input))

user_str = input('What would you like the alphabetize? \n')
print(user_str, 'alphabetized is ', alpha(user_str))