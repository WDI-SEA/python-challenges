# You'll need to use a couple of built in functions to alphabetize a string. 
# Try to avoid looking up the exact answer and look at built in functions for
# lists and strings instead.

word = input("Enter a word to alphabetize.")
# sorted function approach
alpha = ""
for letters in sorted(word):
    alpha += letters

print(alpha)

# convert to list approach
word_list = list(word)
word_list.sort()
string = "".join(word_list)
print(string)