# You'll need to use a couple of built in functions to alphabetize a string. 
# Try to avoid looking up the exact answer and look at built in functions for
# lists and strings instead.

### MY WAY ###
# my_string = input("Enter a string to be sorted: \n")
# sorted_string = sorted(my_string.lower())
# print(''.join(sorted_string))

word = 'banana'
word_li = list(word)
word_li.sort()
new_string = ''.join(word_li)
print(new_string)

