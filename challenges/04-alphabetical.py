# You'll need to use a couple of built in functions to alphabetize a string. 
# Try to avoid looking up the exact answer and look at built in functions for
# lists and strings instead.

# print(dir(list))

# my_li = ['b', 'c', 'a']
# my_li.sort()
# print(my_li)

word = 'supercalifragilisticexpialidocious'
word_li = list(word)
word_li.sort()

# print(str(word_li))

new_string = ''.join(word_li)

# for char in word_li:
#     new_string += char

print(new_string)