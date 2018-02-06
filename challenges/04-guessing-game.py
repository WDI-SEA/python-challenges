from random import randint

MIN = 1
MAX = 100
count = 1
randNum=(randint(MIN, MAX))

guessCount = 0
guessed = False
while guessed==False:
    userInput = int(input("Guess a number between %d and %d:\n" % (MIN, MAX)))
    if userInput==randNum:
        guessCount = guessCount + 1
        guessed = True
        print("Well done!")
    elif userInput>randNum:
        guessCount = guessCount + 1        
        print("the number is lower than", userInput,'. Guess again')
    elif userInput<randNum:
        guessCount = guessCount + 1        
        print("the number is higher than", userInput,'. Guess again')

print("You got it in",guessCount,'tries!')