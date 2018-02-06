from random import randint

MIN = 1
MAX = 100
RANDOM_NUM = randint(MIN, MAX)

def no_match(guess, greaterOrLess):
  new_guess = check_for_match(int(input("%d is %s than the number. Guess again.\n" % (guess, greaterOrLess))), RANDOM_NUM)

def check_for_match(guess, RANDOM_NUM):
	if guess < RANDOM_NUM:
		no_match(guess, "less")
		# total_guesses = total_guesses + 1
		# return total_guesses	
		# print(total_guesses)
		# return total_guesses += increment
		# print(total_guesses)
		# increase_guesses(number_guesses)	
	elif guess > RANDOM_NUM:
		no_match(guess, "more")
		# total_guesses = total_guesses + 1
		# return total_guesses
		# print(total_guesses)
		# return total_guesses += increment
		# print(total_guesses)
		# increase_guesses(number_guesses)
	elif guess == RANDOM_NUM:
		print(f"You guessed it in __ tries!")

# def increase_guesses(number_guesses):
# 	return number_guesses + 1

# number_guesses = increase_guesses(number_guesses)
# print(number_guesses)
# if number_guesses < 2:
guess = check_for_match(int(input("Guess a number between %d and %d\n" % (MIN, MAX))), RANDOM_NUM)


