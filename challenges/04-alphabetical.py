# You'll need to use a couple of built in functions to alphabetize a string. 
# Try to avoid looking up the exact answer and look at built in functions for
# lists and strings instead.

word = 'aipfiugvotybqppojasdjknfviqpihvbdbvaspdfio'

word_li = list(word)

word_li.sort()

string_one = ''
for char in word_li:
  string_one += (char)

print(string_one)
# OR
string_two = ''.join(word_li)
print(string_two)