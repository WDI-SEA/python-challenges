# You'll need to use a couple of built in functions to alphabetize a string. 
# Try to avoid looking up the exact answer and look at built in functions for
# lists and strings instead.

def alphabetize(str):
    # sorted_str = sorted(str)
    
    # stringified = ''.join(sorted_str)

    # return stringified

    return ''.join(sorted(str))

print(alphabetize("supercalifragilisticexpialidocious"))