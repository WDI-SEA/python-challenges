# You'll need to use a couple of built in functions to alphabetize a string. 
# Try to avoid looking up the exact answer and look at built in functions for
# lists and strings instead.


def sort_string():
    sorted_string = ''
    string = input('Give me a string to sort alphabetically: \n')
    sorted_list = sorted(string)
    print('Alpabetized string is: ', sorted_string.join(sorted_list))


sort_string()
