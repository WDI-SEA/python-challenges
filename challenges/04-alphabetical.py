# You'll need to use a couple of built in functions to alphabetize a string. 
# Try to avoid looking up the exact answer and look at built in functions for
# lists and strings instead.

def alphabetize(string):
    new_string = list(string)
    new_string.sort()
    print(new_string)
    string = ''.join(new_string)
    return string
    
print(alphabetize('bombadil'))

