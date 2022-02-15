from random import choice
from toimport import getCharSet, getPositiveInteger

def playOneGame(roundNumber):
    coin = "HhTt"
    tossOutcome = choice(coin)
    guess = getCharSet("Round {}: Head or Tail (H or T): ".format(roundNumber), coin)

    if guess == tossOutcome:
        print("Correct!")
        return 1
    else:
        print("Incorrect.")
        return 0

def lab3Q6b():
    rounds = getPositiveInteger("How many rounds to play?: ")
    wins = 0
    for i in range(1,rounds+1):
        wins = wins + playOneGame(i)

    print("You guess {} correct out {} rounds.".format(wins, rounds))

lab3Q6b()
