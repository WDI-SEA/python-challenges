# You'll need to use a couple of built in functions to alphabetize a string. 
# Try to avoid looking up the exact answer and look at built in functions for
# lists and strings instead.

def isSorted():
    string = input('Enter string to alphabetize\n')
    new_word = ''.join(sorted(string))
    print(f'Alphabetized: {new_word}')


# Without built in function
def sort_str():
    word = input('Enter string to alphabetize\n')
    tem_arr = []
    x = len(word)
    for i in word:
        tem_arr.append(i)

    for i in range(0, x):
        for j in range(0, x):
            if tem_arr[i] < tem_arr[j]:
                temp = tem_arr[i]
                tem_arr[i] = tem_arr[j]
                tem_arr[j] = temp

    new_str = ""
    for i in tem_arr:
        new_str += i

    print(f'Alphabetized: {new_str}')


isSorted()
sort_str()