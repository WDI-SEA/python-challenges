# Create a function that takes a string and returns the string with the letters in alphabetical order (ie. hello becomes ehllo), Assume numbers and punctuation symbols will not be included in the string.

# Give me a string to alphabetize
# supercalifragilisticexpialidocious
# Alphabetized: aaacccdeefgiiiiiiillloopprrssstuux


# You'll need to use a couple of built in functions to alphabetize a string. 
# Try to avoid looking up the exact answer and look at built in functions for lists and strings instead.

# print(dir(str))

def alphabetize_string(string):
    # make the string into a list
    ordered_list = list(string)
    # sort letters in alphabetical order using .sort method
    ordered_list.sort()
    # join the letters back together
    ordered_string = ''.join(ordered_list)
    return ordered_string
print(alphabetize_string('supercalifragilisticexpialidocious'))