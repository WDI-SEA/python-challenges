import random

attempts = 10
guess_number = random.randint(1,100)

for attempt in range(attempts):
    guess - int(input('take a guess: '))

    if guess < secret_number:
        print('higher...')
    elif guess > guess_number:
        print('lower...')
    else:
        print('you guessed it the number is', guess_number)
        print('number of guesses', attempts, 'attempts')

if guess != guess_number:
print()
print('sorry max tries reached')
print('the number was', guess_number)

