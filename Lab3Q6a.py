from random import choice
from toimport import getCharSet

def lab3Q6a():
    coin = "HhTt"
    tossOutcome = choice(coin)
    guess = getCharSet("Head or Tail (H or T): ", coin)

    if guess == tossOutcome:
        print("Correct!")
    else:
        print("Incorrect.")



#lab3Q6a()