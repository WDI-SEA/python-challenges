# You'll need to use a couple of built in functions to alphabetize a string. 
# Try to avoid looking up the exact answer and look at built in functions for
# lists and strings instead.

string = "Its only a flesh wound"
alp_string = sorted(string.lower())
print("" .join(alp_string))

# ==============review answer ====================
print(dir(list))

my_list = ["my string"]
my_list.sort()
print(my_list)

word = "longassword"
# conver string to list
word_list = list(word)

# sort list
word_list.sort()
# convert string to list
new_string = "".join(word_list)

print(new_string)



# print