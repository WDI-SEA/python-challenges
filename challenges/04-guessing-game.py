from random import randint

MIN = 1
MAX = 100

correct_answer = randint(MIN, MAX)
initial_guess = input("Guess a number between %d and %d \n" % (MIN, MAX))
initial_guess = int(initial_guess)

def evaluate_guess(guess):
	if(guess > correct_answer):
		guess = input("The number is lower than {}.  Guess again \n".format(guess))
		guess = int(guess)
		return guess 
	elif (guess < correct_answer):
		guess = input("The number is higher than {}.  Guess again \n".format(guess))
		guess = int(guess)
		return guess 


def guessing_game(guess):
	count = 1;
	while guess != correct_answer:
		guess = evaluate_guess(guess)
		count = count +1
		
	print('You got it in {} tries'.format(count))
	

guessing_game(initial_guess)
