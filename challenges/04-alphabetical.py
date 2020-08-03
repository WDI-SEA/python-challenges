# You'll need to use a couple of built in functions to alphabetize a string. 
# Try to avoid looking up the exact answer and look at built in functions for
# lists and strings instead.
def alphabetize(string):
    # take in string and cast to list type
    new_list = list(string)
    # print(new_list)
    # run sort on list
    new_list.sort()

    new_string = ""

    for letter in new_list:
        new_string = new_string + letter

    return new_string

print(alphabetize("asfdkjgajkgulgiah"))