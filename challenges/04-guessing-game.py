from random import randint

MIN = 1
MAX = 10
TARGETNUM = randint(MIN, MAX)

def guessing_game(num=None, this_turn=0):
    turn = this_turn + 1
    if(num is None):
        guess = int(input('Guess a number between {} and {}\n'.format(MIN, MAX)))
        guessing_game(guess, turn)
    elif(num > MAX or num < MIN):
        guess = int(input('Quit trying to break things. Pick again.\n'))
        guessing_game(guess, turn)
    elif(num != TARGETNUM):
        position = 'higher' if num < TARGETNUM else 'lower'
        guess = int(input('The number is {} than {}. Guess again\n'.format(position, num)))
        guessing_game(guess, turn)
    else: 
        print('You got it in {} tries'.format(this_turn))

guessing_game()