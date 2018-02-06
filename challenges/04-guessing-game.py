# Create a program that asks the user to guess a number between 1 and 100. Once the user guesses a number, 
# the program should say, higher, lower, or tell the user that he got the number correct. 
# The user should continue to make guesses until he guesses correctly. Also, once the user guesses correctly, 
# the program should print the number of guesses needed to arrive at the correct answer. Below is sample output:

# Guess a number between 1 and 100
# 50
# The number is lower than 50.  Guess again
# 25
# The number is lower than 25.  Guess again
# 13
# The number is higher than 13.  Guess again
# 20
# The number is lower than 20.  Guess again
# 17
# The number is higher than 17.  Guess again
# 18
# The number is higher than 18.  Guess again
# 19
# You got it in 7 tries

from random import randint

MIN = 1
MAX = 5
tries = 0

def guess_number():
  number = randint(MIN, MAX)
  guess = int(input("Guess a number between %d and %d" % (MIN, MAX)))
  if guess < number:
    print("The number is higher than {}. Guess again".format(guess))
    tries = tries + 1
  elif guess > number:t
    print("The number is lower than {}. Guess again".format(guess))
    tries = tries + 1
  elif guess == number:
    print("Yep! You got it in {} tries.".format(tries))
  else:
    print("Pls guess a real number")

  guess_number()


