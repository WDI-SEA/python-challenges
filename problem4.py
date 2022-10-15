#Create a function that takes a string and returns the string with the letters in alphabetical order (ie. hello becomes ehllo), Assume numbers and punctuation symbols will not be included in the string.

# word = "test"

# sorted = sorted(word)

# formatted = "".join(sorted)

# print(formatted)

def alphabatizer():
  prompt = input("Please input the word you want to alphabatize: ")
  user_word = str(prompt)
  user_sorted = sorted(user_word)
  formatted = "".join(user_sorted)
  print(f"Alphabatized: {formatted}")

alphabatizer()
