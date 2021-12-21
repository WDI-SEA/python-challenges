# You'll need to use a couple of built in functions to alphabetize a string. 
# Try to avoid looking up the exact answer and look at built in functions for
# lists and strings instead.

string = input('What would you like me to alphabetize: \n')

def split(word):
    return [letter for letter in word]

split_string = split(string)

split_string.sort()

result = "".join(split_string)

print(result)

# print(' '.join(split_string.sort()))