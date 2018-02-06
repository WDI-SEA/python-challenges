# from random import randint
#
# MIN = 1
# MAX = 5
#
# print("Guess a number between %d and %d" % (MIN, MAX))
# print("Delete me. Here's a random number:", randint(MIN, MAX))

import random # imported random module
rand = random.randint(1,100)
guesses = 0

def find_num():
  guess = input('Guess a number between 1 and 100...\n')
  guess = int(guess)
  if (rand > guess):
    print('Too low, try again')
    guesses + 1
    find_num()
  elif (rand < guess):
    print('Too high, try again')
    guesses + 1
    find_num()
  elif (rand == guess):
    print('You won! And in so many guesses', guesses)
  else:
    print('you must input an integer in the range')
    find_num()

find_num()
