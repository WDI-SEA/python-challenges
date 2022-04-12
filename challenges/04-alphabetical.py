a_string = input("please enter a word: ")
an_array = list(a_string)
new_array = []
for char in an_array:
    new_array.append(char)
    listToStr = (''.join(map(str, new_array)))
    sorted_word = sorted(listToStr)
    join_the_sorted_word = (''.join(map(str, sorted_word)))
print(join_the_sorted_word )