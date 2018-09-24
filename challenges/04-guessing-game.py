from random import randint

answer = randint(1, 10)

print("I'm thinking of a number between 1 and 10.")

while True:
	try:
		guess = int(input("Please guess my number:"))
	except:
		print("That's not a number")
		continue
	if guess < answer:
		print("Haha! Too low!")
	elif guess > answer:
		print("Haha! Too high!")
	else:
		print("Aww, you got it.")
		break