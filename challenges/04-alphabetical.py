# You'll need to use a couple of built in functions to alphabetize a string. 
# Try to avoid looking up the exact answer and look at built in functions for
# lists and strings instead.


string = input('Give me a string to alphabetize\n')

def alphabetize(str_input):
    letter_list = ('abcdefghijklmnopqrstuvwxyz')
    alphabetized = ''
    string_list = list(str_input) 
    string_list.sort()
    for letter in string_list:
        if letter.lower() in letter_list:
            alphabetized += letter
    return alphabetized

print('Alphabetized : {}'.format(alphabetize(string))) 