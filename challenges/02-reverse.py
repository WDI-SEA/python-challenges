
a_string = input("please enter a string: ")
an_array = list(a_string)
new_array = []
for char in an_array:
    new_array.append(char)
    list.reverse(new_array)
    listToStr = ''.join(map(str, new_array))
print(listToStr)

