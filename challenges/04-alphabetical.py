# You'll need to use a couple of built in functions to alphabetize a string. 
# Try to avoid looking up the exact answer and look at built in functions for
# lists and strings instead.

# def sort_letters(string):
#     print(''.join(sorted(string)))

# sort_letters('snappleapplepie')

def sort_letters(string):
    arr = []
    for letter in string:
        arr.append(letter)
    arr.sort()
    result = ''.join(arr)

    print(result)
    
    

sort_letters('snappleapplepie')
sort_letters('supercalifragilisticexpialidocious')