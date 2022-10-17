# You'll need to use a couple of built in functions to alphabetize a string. 
# Try to avoid looking up the exact answer and look at built in functions for
# lists and strings instead.

## MY METHOD
# string = input('Give me a string to alphabetize\n')
# string_list = sorted(string)

# def alphabetize_string(string):
#     return ''.join(sorted(string))
# print(alphabetize_string(string))

# print(string_list)


## # ## # DELIVERABLE REVIEW

# print(dir(list))
# my_li = ['b','c','a']
# my_li.sort()
# print(my_li)

word = 'supercalifragilisticexpialidocious'
#CONVERT string to list
word_li = list(word)
# print(word_li)

#SORT list
word_li.sort()
print(word_li)

#CONVERT list to string
new_string = ''.join(word_li)
# for char in word_li:
#     new_string += char

print(new_string)

