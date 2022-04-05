# You'll need to use a couple of built in functions to alphabetize a string. 
# Try to avoid looking up the exact answer and look at built in functions for
# lists and strings instead.
import string

def alphabetize(user_string):
    alphabet_string = string.ascii_lowercase
    positions = []
    for i in range(0, len(user_string)):
        positions.append(alphabet_string.index(user_string[i]))
        sorted_positions = sorted(positions)
    for i in range(0, len(sorted_positions)):
        sorted_positions[i] = alphabet_string[sorted_positions[i]]
    print(sorted_positions)
alphabetize('whatisthis')