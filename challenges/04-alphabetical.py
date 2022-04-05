# You'll need to use a couple of built in functions to alphabetize a string. 
# Try to avoid looking up the exact answer and look at built in functions for
# lists and strings instead.

# def alphabetize(string):
#     # print(dir(str))

    
#     # needs to loop through each letter in the word
#     # each time it sees a letter, print it out before moving to the next letter of the alphabet
#     # return reverse

# alphabetize("hello")


string = input('Give me a string to alphabetize\n')
# turn the string into a list - to get access to each individual letter
listed_string = list(string) 
# sort all the letters alphabetically
listed_string.sort()

alphabetized = ''
for letter in listed_string:
    alphabetized += letter

print(alphabetized)