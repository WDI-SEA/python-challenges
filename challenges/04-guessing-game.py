from random import randint

MIN = 1
MAX = 100
number = randint(MIN, MAX)
count = 0

guess = int(input("Guess a number between %d and %d \n" % (MIN, MAX)))

def guessagain(guesses, newCount):
	if guesses > number:
		newCount += 1
		guesses = int(input("The number is lower than {}. Guess again. \n".format(guesses)))
		guessagain(guesses, newCount)
	elif guesses < number:
		newCount += 1
		guesses = int(input("The number is greater than {}. Guess again. \n".format(guesses)))
		guessagain(guesses, newCount)
	elif guesses == number:
		print("you got it! The number is {}. You got it in {} guess".format(number, newCount + 1))

def guessing():
	if guess > number:
		guesses = int(input("The number is lower than {}. Guess again. \n".format(guess)))
		newCount = count + 1
		guessagain(guesses, newCount)
	elif guess < number:
		guesses = int(input("The number is greater than {}. Guess again. \n".format(guess)))
		newCount = count + 1
		guessagain(guesses, newCount)
	elif guess == number:
		print("you got it! The number is {}. You got it in {} guess".format(number, count + 1))

guessing()
