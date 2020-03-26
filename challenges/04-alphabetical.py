# You'll need to use a couple of built in functions to alphabetize a string. 
# Try to avoid looking up the exact answer and look at built in functions for
# lists and strings instead.

print("Give me a string to alphabetize")
user_string = input().lower()

temp_dict = {}

for index, letter in enumerate(user_string):
  temp_dict[index] = letter

print(temp_dict)


for index in temp_dict:
  print(index)
  if temp_dict[index + 1]:
    if temp_dict[index] > temp_dict[index + 1]:
      temp_letter = temp_dict[index]
      temp_dict[index] = temp_dict[index + 1]
      temp_dict[index + 1] = temp_letter

print(temp_dict)

print(f"Alphabetized: {user_string}")

# Give me a string to alphabetize
# supercalifragilisticexpialidocious
# Alphabetized: aaacccdeefgiiiiiiillloopprrssstuux