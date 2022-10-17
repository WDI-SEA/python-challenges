# You'll need to use a couple of built in functions to alphabetize a string. 
# Try to avoid looking up the exact answer and look at built in functions for
# lists and strings instead.


# print(dir(str))


# my_list = ['b', 'c', 'a']
# my_list.sort()
# print(my_list)

word = 'happy'
word_list = list(word)
word_list.sort()
print(str(word_list))

new_string = ''
for char in word_list:
    new_string += char

print(new_string)