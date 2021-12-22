# You'll need to use a couple of built in functions to alphabetize a string. 
# Try to avoid looking up the exact answer and look at built in functions for
# lists and strings instead.

def sort(string):
    sort_list = []
    for letter in string:
        sort_list.append(letter)
    sort_list.sort()
    print("".join(sort_list))

sort("supercalifragilisticexpialidocious")