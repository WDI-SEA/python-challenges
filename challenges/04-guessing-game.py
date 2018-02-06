from random import randint

MIN = 1
MAX = 100

# print("Guess a number between %d and %d" % (MIN, MAX))
print("Delete me. Here's a random number:", randint(MIN, MAX))


guess = input("Guess a number between %d and %d\n" % (MIN, MAX))
guess = int(guess)
random = randint(MIN, MAX)
total = 0
if(guess == random):
	print("You got it! The number is ", random, " guessed in ", total, "tries")
elif(guess < random):
	print("The number is higher than ", guess, ". Try again!\n")
	total += 1
	guess = input("Try again!\n")
else:
	print("The number is lower than ", guess, ". Try again!\n")
	total += 1
	guess = input("Try again!\n")


