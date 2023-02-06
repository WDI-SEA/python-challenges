# You'll need to use a couple of built in functions to alphabetize a string. 
# Try to avoid looking up the exact answer and look at built in functions for
# lists and strings instead.

# Give me a string to alphabetize
# supercalifragilisticexpialidocious
# Alphabetized: aaacccdeefgiiiiiiillloopprrssstuux

print('Alpahbetizer.exe Type in anything to sort them in alphabetical order')
word = input()

def alphabetize(word):
    # print(word)
    sorted_word = sorted(word)
    print(''.join(sorted_word))

alphabetize(word)