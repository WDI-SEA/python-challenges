# You'll need to use a couple of built in functions to alphabetize a string. 
# Try to avoid looking up the exact answer and look at built in functions for
# lists and strings instead.

# Create a function that takes a string and returns the string with the letters in alphabetical order (ie. hello becomes ehllo), Assume numbers and punctuation symbols will not be included in the string.
string = input("Give me a string to alphabetize:\n")
sorted_list = sorted(string)
string_alphabetized = "".join(sorted_list)
print("Alphabetized:", string_alphabetized



# Give me a string to alphabetize
# supercalifragilisticexpialidocious
# Alphabetized: aaacccdeefgiiiiiiillloopprrssstuux