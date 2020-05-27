# You'll need to use a couple of built in functions to alphabetize a string. 
# Try to avoid looking up the exact answer and look at built in functions for
# lists and strings instead.

alphabet = 'I like 2345 @ python!!!'
another = 'supercalifragilisticexpialidocious'

def sort_alphabetically():
    var = input("Enter a text or string\n")
    sorted_list = sorted(list(var))
    sorted_list= "".join(sorted_list)
    sorted_list = sorted_list.replace(" ", "")  # for removing spaces in the sentence
    return sorted_list

print(sort_alphabetically())


str= "".join(sorted("I like 2345 @ python!!!"))
print(str)