# You'll need to use a couple of built in functions to alphabetize a string. 
# Try to avoid looking up the exact answer and look at built in functions for
# lists and strings instead.

def alphabetize_string(string):
    alphabetized_string = ''.join(sorted(string))
    return alphabetized_string

input_string = input("Give me a string to alphabetize:\n")
result = alphabetize_string(input_string)
print("Alphabetized:", result)
