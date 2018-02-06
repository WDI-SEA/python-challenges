#from random import randint

#MIN = 1
#MAX = 5

#print("Guess a number between %d and %d" % (MIN, MAX))
#print("Delete me. Here's a random number:", randint(MIN, MAX))

#Create a program that asks the user to guess a number between 1 and 100. 
#Once the user guesses a number, the program should say, higher, lower, or 
#tell the user that he got the number correct. The user should continue to make guesses 
#until he guesses correctly. Also, once the user guesses correctly, the program should print the 
#number of guesses needed to arrive at the correct answer. Below is sample output:

#Guess a number between 1 and 100
#50
#The number is lower than 50.  Guess again
#25
#The number is lower than 25.  Guess again
#13
#The number is higher than 13.  Guess again
#20
#The number is lower than 20.  Guess again
#17
#The number is higher than 17.  Guess again
#18
#The number is higher than 18.  Guess again
#19
#You got it in 7 tries


import random
n = random.randint(1, 99)
guess = int(input("Enter an integer from 1 to 100: "))
while n != "guess":
    print
    if guess < n:
        print ('guess is low')
        guess = int(input("Enter an integer from 1 to 99: "))
    elif guess > n:
        print ('guess is high')
        guess = int(input("Enter an integer from 1 to 99: "))
    else:
        print ('you guessed it!')
        break
    print