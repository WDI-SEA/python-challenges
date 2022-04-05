# You'll need to use a couple of built in functions to alphabetize a string. 
# Try to avoid looking up the exact answer and look at built in functions for
# lists and strings instead.


#

def alphabetize(string):
    new_list = list(string)
    new_list.sort()

    new_string = ""
    for letter in new_list:
        new_string = new_string + letter
        return new_string

print(alphabetize('supercalifragilisticexpialidocious'))

my_str = input('your string now? ')
my_list = list(my_str)
my_list.sort()

alpha_str = ''.join(my_list)
print(alpha_str)