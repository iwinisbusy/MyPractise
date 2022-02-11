
"""
A telco charges the following for usage of data in a foreign country:
    Data            Rate
    Up to 2GB       $5 flat
    Above 2GB       $5 + $1 for every 100MB or part thereof

Two example runs are shown here:

Run 1:
Amount of data used (GB): 1.5
Charge is $5.00

Run 2:
Amount of data used (GB): 2.54    2.1
Charge is $11.00                  $6

(Make use of the ceil() function from Math library)
"""

import math

def lab2_q5():
    data = float(input('Enter amount of data used (GB): '))
    data = data * 1000  # all to MB
    if data <= 2000:
        charge = 5
    else:
        #print((data - 2000)/100)
        charge = math.ceil((data - 2000)/100) + 5

    print(f'Charge is ${charge:.2f}')
    
lab2_q5()