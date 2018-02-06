
from random import randint

MIN = 1
MAX = 100

num = randint(MIN, MAX)
guess = MAX + 1
i = 0


print("Guess a number between %d and %d" % (MIN, MAX))
while(int(guess) != num):
  guess = input()
  if(int(guess) < num):
    print('The Number is higher than', guess, 'try again')
  elif(int(guess) > num):
    print('The Number is lower than', guess, 'try again')
  i += 1
print('You got it right in', i, 'tries')