from random import choice
from toimport import getCharSet

def lab3Q6a():
    coin = "HhTt"
    tries = 0

    while True:
        tossOutcome = choice(coin)
        tries += 1
        guess = getCharSet("Head or Tail (H or T): ", coin)

        if guess == tossOutcome:
            print("Correct!")
            break
            
        else:
            print("Incorrect.")
    
    print("You have tried: {} times".format(tries))


lab3Q6a()

