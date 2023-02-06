# You'll need to use a couple of built in functions to alphabetize a string. 
# Try to avoid looking up the exact answer and look at built in functions for
# lists and strings instead.

user_word = input('Type a word you want to see alphabetically:\n> ')

def alphabetize(word):
    alphabetized_word = ''
    for letter in (sorted(word)):
        alphabetized_word += letter
    print(alphabetized_word)

alphabetize(user_word)