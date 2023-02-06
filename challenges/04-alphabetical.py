# You'll need to use a couple of built in functions to alphabetize a string. 
# Try to avoid looking up the exact answer and look at built in functions for
# lists and strings instead.
# print(dir([]))
array = ['a', 'l', 'q', 'c', 'j']
array.sort()
# print(''.join(array))

def alphebetize():
    # string = []
    print('give string to alph \n                   ;-;')
    print(''.join(sorted(input())))
    # for letter in input():
    #     string.append(letter)
    #     string.sort()
    # print(''.join(string))

# alphebetize()


def sort_string(string):
    temp_li = list(string)
    temp_li.sort()
    return ''.join(temp_li)
print(sort_string('aaaerejkjjllldfjoeirjer'))