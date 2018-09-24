from random import randint

MIN = 1
MAX = 5

to_guess = randint(MIN, MAX)

print('I\'m thinking of a number between {} and {}'.format(MIN,MAX))

user_guess = to_guess + 1

while user_guess != to_guess:
    try:
        user_guess = int(input('Please guess what it is: ')) 
    except:
        print('That is not a number!')
        continue
    if user_guess > to_guess:
        print('Too high!')
    elif user_guess < to_guess: 
        print('Too low!')

print('You guessed correctly! The anser was {}'.format(user_guess))
