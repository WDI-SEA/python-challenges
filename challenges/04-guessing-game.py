from random import randint
from random import randint

MIN = 1
MAX = 100

print("Guess a number between %d and %d\n" % (MIN, MAX))
answer = randint(MIN, MAX)
number_guessed = False
guesses = 0
while(number_guessed is False):
  guess = input('Guess a number\n')
  guesses += 1
  try:
    int_guess = int(guess)
  except:
    print('That\'s not a number')
    continue
  if (int_guess == answer):
    number_guessed = True
    print(f'You guessed it right in {guesses} guesses!')
  elif ( int_guess > answer):
    print(f'The number is lower than {guess}.')
  elif ( int_guess < answer):
    print(f'The number is higher than {guess}.')
