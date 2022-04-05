# You'll need to use a couple of built in functions to alphabetize a string. 
# Try to avoid looking up the exact answer and look at built in functions for
# lists and strings instead.

# def sort(string): 
#     temp = {}
#     # do a letter count
#     for letter in string:
#         if letter in temp:
#             temp[letter] += 1
#         else:
#             temp[letter] = 1
    
#     # then alphabetize the keys
#     for letter in temp.keys():
#         if letter > (letter + 1):
#             letter = letter + 1
        
#         print(letter)
        
#     # print the keys, item-times

# print(
# sort('supercalifragilisticexpialidocious')
# )

def sort(string):
    string = sorted(string)
    string = ''.join(string)
    return string

print(sort('supercalifragilisticexpialidocious'))