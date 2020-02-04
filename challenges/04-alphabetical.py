# You'll need to use a couple of built in functions to alphabetize a string. 
# Try to avoid looking up the exact answer and look at built in functions for
# lists and strings instead.
def alphabetical(str):
    str_sort = sorted(str)
    alpha_str = ''.join(str_sort)
    print(alpha_str)
    
alphabetical('supercalifragilisticexpialidocious')