# You'll need to use a couple of built in functions to alphabetize a string. 
# Try to avoid looking up the exact answer and look at built in functions for
# lists and strings instead.
# Alphabatize the letters in a letter-only string
alphabet = 'abcdefghijklmnopqrstuvwxyz'
def alphabetical(phrase):
    # Set the input to a list so it's easier to manipulate
    phrase = list(phrase) # Make phrase.lower() if you want case insensitivity
    # It's basically a bubble-up function
    for i in range(1,len(phrase)):
        # Create a variable to track progress in the bubbling
        place = i
        # While the current char can bubble up and has room to do so
        while(phrase[place] < phrase[place-1] and place > 0):
            # Perform a good ol' swap function
            temp            = phrase[place]
            phrase[place]   = phrase[place-1]
            phrase[place-1] = temp
            # Iterate the place down to repeat the process
            place -= 1
    # And you're done! It even works for non-letter characters
    return ''.join(str(letter) for letter in phrase)

print(alphabetical('Hello My wonderful friends!!!'))