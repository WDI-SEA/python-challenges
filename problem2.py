# Reverse a string manually. Don't use s[::-1] (even though that's awesome). Create a new variable storing an empty string and add the letters from the first string one by one. The for loop should iterate over the length of the string and you should access letters individually.
# my_word = "stock"
# new_word =""

# i = len(my_word) - 1

# while i >= 0:
#   new_word = my_word[i]
#   i -= 1
#   print(new_word)


word = input("type a word: ")
reversed = ""
for letter in word:
    reversed = letter + reversed

print(reversed)

