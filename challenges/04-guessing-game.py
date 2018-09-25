from random import randint

#import random
def guessingGame2():
    result = random.randint(1,100)
    count = 1
    while True:
        guess = int(input('Guess a number between 1 and 100'))
        if (guess < result):
            print(f'The number is larger than {guess} . Guess again')
            count+=1
        elif(guess > result):
            print(f'The number is smaller than {guess}. Guess again')
            count+=1
        else:
            print(f'You got it in {count} tries')
            break

guessingGame2()
