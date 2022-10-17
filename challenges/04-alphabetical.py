# You'll need to use a couple of built in functions to alphabetize a string. 
# Try to avoid looking up the exact answer and look at built in functions for
# lists and strings instead.


# ### Challenge 4 - Sort a String

# Create a function that takes a string and returns the string with the letters in 
# alphabetical order (ie. `hello` becomes `ehllo`), Assume numbers and punctuation 
# symbols will not be included in the string.

# ```
# Give me a string to alphabetize
# supercalifragilisticexpialidocious
# Alphabetized: aaacccdeefgiiiiiiillloopprrssstuux
# ```

word = 'supercalifragilisticexpialidocious'

# convert string to list
word_li = list(word)

# sort list
word_li.sort()

# convert list to string
new_string = ''.join(word_li)
# for char in word_li:
#     new_string += char

print(new_string)
# print(dir(list))

# my_li = ['b', 'c', 'a']
# my_li.sort()
# print(my_li)