from random import randint

MIN = 1
MAX = 50

# print("Guess a number between %d and %d" % (MIN, MAX))
# print("Delete me. Here's a random number:", randint(MIN, MAX))


random_number = randint(MIN, MAX)
# print(random_number)
guess = int(input("Enter you guessed number from 1 to 50: \n"))

times = 0
while random_number != guess:
    if guess < random_number:
        print ("guess is low")
        guess = int(input("Enter an integer from 1 to 50: \n"))
        times += 1
    elif guess > random_number:
        print ("guess is high")
        guess = int(input("Enter an integer from 1 to 50: \n"))
        times += 1
print ("you guessed it!")
print ('You got it in {} tries'.format(times))

    