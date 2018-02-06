from random import randint

MIN = 1
MAX = 100

print("Guess a number between {0} and {1}".format(MIN, MAX))
number_to_guess = (randint(MIN, MAX))
user_input = None
counter = 1
while (number_to_guess != user_input):
  
  user_input = input('Please enter a number: ')
  user_input = int(user_input)
  
  if (user_input > number_to_guess):
    print('Number is lower than {}.'.format(user_input))
    counter +=1
  elif(user_input < number_to_guess):
    print('Number is higher than {}.'.format(user_input))
    counter +=1
  else:
    print('You guessed the number in {} tries'.format(counter))
