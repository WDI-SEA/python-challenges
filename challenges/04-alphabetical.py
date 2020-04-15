# You'll need to use a couple of built in functions to alphabetize a string. 
# Try to avoid looking up the exact answer and look at built in functions for
# lists and strings instead.

# Give me a string to alphabetize
# supercalifragilisticexpialidocious
# Alphabetized: aaacccdeefgiiiiiiillloopprrssstuux

string = 'supercalifragilisticexpialidocious'

def split(string):
  return list(string)

new_string = split(string)
alpha = sorted(new_string)
final_string = "".join(alpha)
print(final_string)

