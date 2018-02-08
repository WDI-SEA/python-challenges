from random import randint

MIN = 1
MAX = 5

target = randint(MIN, MAX)

def checkGuess(guess, target, tries, min, max):
	try:
		guess = int(guess)
		if guess not in range(min, max+1):
			print("Out of range! The number is betwen %d and %d" % (min, max))
		elif guess==target:
			return "That's it! The number is "+str(target)+". You got it in "+str(tries)+" tries."
		elif guess<target:
			print("The number is higher than "+str(guess)+".")
		elif guess>target:
			print("The number is lower than "+str(guess)+".")
	except:
		print("Whoah, we're working with integers here!")
	tries +=1
	guess = input("Guess again!\n")
	return checkGuess(guess, target, tries, min, max)

print("Guess a number between %d and %d." % (MIN, MAX))
guess = input()
print(checkGuess(guess, target, 1, MIN, MAX))



