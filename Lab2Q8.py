"""
8. Modify the program in question 2 with the following rate:

    Data            Rate
    Up to 2GB       $5 flat
    Above 2GB       $5 + $1 for every 100MB or part thereof
    Above 4GB       $25 flat

The program also validates that input must be greater than 0. Otherwise, display “Invalid input!”.
"""


import math

def lab2_q8():
    data = float(input('Enter amount of data used (GB): '))

    if data <= 0:
        print("Invalid input!")
    else:
        data = data * 1000  # all to MB
        if data <= 2000:
            charge = 5
        elif data <= 4000:
            #print((data - 2000)/100)
            charge = math.ceil((data - 2000)/100) + 5
        else:
            charge = 25

        print(f'Charge is ${charge:.2f}')
    
lab2_q8()