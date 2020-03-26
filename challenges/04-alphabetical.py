# You'll need to use a couple of built in functions to alphabetize a string. 
# Try to avoid looking up the exact answer and look at built in functions for
# lists and strings instead.
def alphabetize(working_string):
    working_string_object = {
        "length": len(working_string)
    }

    for index in range(len(working_string)):
        working_string_object[index] = working_string[index]
        
    alphabetized_string = alphabetize_sort(working_string_object)
    printable_string = transform(alphabetized_string)
    return printable_string

def transform(working_string):
    return_string = ''
    for index in range(len(working_string) - 1):
        return_string += working_string[index]
    return return_string

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

user_input = input("Give me a string to alphabetize" + '\n')
alphabetized_input = alphabetize(user_input)
print(alphabetized_input)