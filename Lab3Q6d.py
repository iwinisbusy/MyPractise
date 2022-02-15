from random import choice
from toimport import getCharSet

def playGame():
    coin = "HhTt"
    noOfTries = 0
    while True:
        tossOutcome = choice(coin)
        print(tossOutcome)
        noOfTries += 1
        guess = getCharSet("Head or Tail (H or T): ", coin)

        if guess == tossOutcome:
            print("Correct!")
            break
        else:
            print("Incorrect.")

    print("You got it in {} tosses!".format(noOfTries))

#lab3Q6d
def main():
    while True:
        playGame()
        stop = input("Play again? (y/n): ")
        if stop[0] in "Nn":
            break
        
    print("Program end")

main()