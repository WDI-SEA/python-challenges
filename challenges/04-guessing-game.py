from random import randint

MIN = 1
MAX = 500

print("Guess a number between %d and %d" % (MIN, MAX))
answer = randint(MIN, MAX)
tries=0
guess=0

while (guess != answer):
    guess = input(":")
    guess = int(guess)

    tries+=1

    if(guess<answer):
        print("The number is higher than %d" % (guess))
    if(guess>answer):
        print("The number is lower than %d" %(guess))

print("You got it! Took you %d tries." %(tries))
