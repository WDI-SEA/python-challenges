# You'll need to use a couple of built in functions to alphabetize a string. 
# Try to avoid looking up the exact answer and look at built in functions for
# lists and strings instead.

word = input("Type a word!\n")

sorted_word = sorted(word)

word = "".join(sorted_word)

print(word)
