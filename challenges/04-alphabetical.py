# You'll need to use a couple of built in functions to alphabetize a string. 
# Try to avoid looking up the exact answer and look at built in functions for
# lists and strings instead.
def alphabetize(working_string):
    # create an object to store the strings information
    working_string_object = {
        "length": len(working_string)
    }

    # store each letter of working_string : working_string[index] = letter
    for index in range(len(working_string)):
        working_string_object[index] = working_string[index]

    # sort working_string_object 
    alphabetized_string = alphabetize_sort(working_string_object)
    printable_string = transform(alphabetized_string)
    return printable_string

# build a string out of the working_string object
def transform(working_string):
    return_string = ''
    for index in range(len(working_string) - 1):
        return_string += working_string[index]
    return return_string

# recursive bubble sort
def alphabetize_sort(working_string_object):
    working_string_object
    swapped = False
    for x in range(0, working_string_object["length"] - 1):
        if working_string_object[x] > working_string_object[x + 1]:
            temp = working_string_object[x]
            working_string_object[x] = working_string_object[x + 1]
            working_string_object[x + 1] = temp
            swapped = True
    if swapped:
        return alphabetize_sort(working_string_object)
    else:
        return working_string_object

# get input string from console
user_input = input("Give me a string to alphabetize" + '\n')

# sort the input and print it out
alphabetized_input = alphabetize(user_input)
print(alphabetized_input)