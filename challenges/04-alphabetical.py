# You'll need to use a couple of built in functions to alphabetize a string. 
# Try to avoid looking up the exact answer and look at built in functions for
# lists and strings instead.

def alphabetize(string):
    alpha_list = sorted(string)
    alpha_string = ''
    for i in alpha_list:
        alpha_string = f"{alpha_string}{i}"
    return alpha_string


print(alphabetize("alphabet"))