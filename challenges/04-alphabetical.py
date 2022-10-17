# You'll need to use a couple of built in functions to alphabetize a string. 
# Try to avoid looking up the exact answer and look at built in functions for
# lists and strings instead.


word = 'Lorem ipsum dolor sit amet consectetur adipiscing elit sed do eiusmod tempor incididunt ut labore et dolore magna aliqua'

# convert string to list
word_li = list(word)

# sort list
word_li.sort()

# convert list to string
new_string = ''
for char in word_li:
     new_string += char

print(new_string)
