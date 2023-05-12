# You'll need to use a couple of built in functions to alphabetize a string. 
# Try to avoid looking up the exact answer and look at built in functions for
# lists and strings instead.

word = input("Enter a word to alphabetize.")

alpha = ""
for letters in sorted(word):
    alpha += letters

print(alpha)
