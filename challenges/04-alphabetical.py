# You'll need to use a couple of built in functions to alphabetize a string. 
# Try to avoid looking up the exact answer and look at built in functions for
# lists and strings instead.


# Create a function that takes a string and returns the string with the letters in 
# alphabetical order (ie. `hello` becomes `ehllo`), Assume numbers and punctuation 
# symbols will not be included in the string.

word = 'supercalifragilisticexpialidocious'

word_li = list(word)
word_li.sort
print(word_li)
new_string = "".join(word_li)


print(dir(list))

my_li ['b', 'c', 'a']
my_li.sort()
print(my_li)