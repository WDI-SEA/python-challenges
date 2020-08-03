# You'll need to use a couple of built in functions to alphabetize a string. 
# Try to avoid looking up the exact answer and look at built in functions for
# lists and strings instead.

# if 'a' > 'b':

#     print("truthy")

# elif 'a' < 'b':

#     print('ordered')

# else:

#     print('third')

#helper function for aphabetize
#return smallest alphabetic character in string
#getSmallest('abc') returns 'a'
#getSmallest('cab') returns 'a'
#getSmallest('gds') returns 'd'

print(min('asdffsa'))
print(min('graeihuhg'))


sortedWord = ""

print('Enter a word to be sorted (alphabetically): ')
word = input()
wordLength = len(word)


###test function
print(f'find(min(word)) : {word.find(min(word))}')

def alphabetize(s):
    global sortedWord
    global wordLength
    for i in range(0, wordLength, 1):
        #debug index
        print(f'wordLength: {wordLength}')
        print(f'index: {i}')
        if i + 1 == wordLength:
            sortedWord = sortedWord + s[0]
            print(sortedWord)
            print('completed')
            quit()
        else:
            #append smallest present character to sorted word
            sortedWord = sortedWord + min(s)
            #find() index of smallest character in s, assign it to smallIndex
            smallIndex = s.find(min(s))
            #alter s to remove character at smallIndex
            s = s[0:smallIndex:1] + s[smallIndex + 1:: 1]
            print(s)
            print(sortedWord)

        # print(sortedWord)


#word with first letter removed
# print(word[1::])
#word with second letter removed
# print(word[0:1:1] + word[2::1])
alphabetize(word)
