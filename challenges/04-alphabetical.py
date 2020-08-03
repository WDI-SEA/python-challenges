# You'll need to use a couple of built in functions to alphabetize a string. 
# Try to avoid looking up the exact answer and look at built in functions for
# lists and strings instead.

string = "supercalifragilisticexpialidocious"

def split(string):
    return list(string)

string2 = split(string)
test = sorted(string2)
output = "".join(test)

print(output)

"""
OUTPUT
aaacccdeefgiiiiiiillloopprrssstuux
"""