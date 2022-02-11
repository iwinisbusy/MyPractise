#Write a program that reads an input representing a change which is an 
#amount less than 1 dollar. The program calculates the change into 50, 10, 5 
#and 1 cent coins. The program then displays the number of each coin
#required for that change. E.g.
#Enter change: 47
#50 cent: 0
#10 cent: 4
#5 cent: 1
#1 cent: 2


def q4():
    pettycash = int(input("Enter change amount: "))
    fifties = pettycash/50
    tens = (pettycash-50)/10
    fives = ((pettycash-50)-10)/5
    ones = pettycash%100
    print("50 cents: ", int(fifties))
    print("10 cents: ", int(round(tens)))
    print("5 cents: ", int(round(fives)))
    print("One cents: ", int(round(ones)))

def lab1_q5():
    # Input: get the change from user
    change = int(input("Enter change: "))


    # Processing:
    # calculate the number of 50 cts
    cents50 = change // 50    # 80 // 50 = 1
    remainder = change - (cents50*50)
    # calculate the number of 10 cts
    cents10 = remainder // 10    # 
    remainder = remainder - (cents10*10)
    # calculate the number of 5 cts
    cents5 = remainder // 5
    # calculate the number of 1 cts
    cents1 = remainder - (cents5*5)

    # display the outcome
    print("50 cent:", cents50)
    print("10 cent:", cents10)
    print("5 cent:", cents5)
    print("1 cent:", cents1)

lab1_q5()
#q4()