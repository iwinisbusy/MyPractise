"""
A computer store allows customers to buy laptops and pay by instalments. The payment plan is based on the purchase amount as given in the following table:

  Amount           Payment
  ======           =======
  Less than 1000 : No instalment. Pay full amount.
  At least 1000  : Either pay in 6 monthly instalments with an addition of 5% of the  
                   amount, or pay in 12 monthly instalments with an addition of 10% of the amount. Payment is the result of adding interest to the amount and then dividing by the number of monthly installments.

Write a program that reads in the amount of the laptop. If the amount is at least 1000, prompt the user to select 0, 6 or 12 months, and display the instalment plan. Examples of different input are as follows:

Run 1   Enter amount: 800 
        Please pay $800.00. No instalment plan.

Run 2   Enter amount: 1200
        Pay in 0, 6 or 12 month instalment: 0 
        Please pay $1200.00. No instalment plan.

Run 3   Enter amount: 2400 
        Pay in 0, 6 or 12 month instalment: 6 
        6 month instalment plan of $420.00 per month

        (Interest on 2400 at 5% for 6 months is 120. Total amount = 2400+120=2520. Divide by 6 = 420)
"""
def lab2_q11():
    # gettting the purchase amount
    cost = float(input('Enter amount: '))

    if cost <= 0:
        print("Invalid amount")
    elif cost < 1000:
        print ('Please pay ${:,.2f}. No installment plan.'.format(cost))
    else:
        month = int(input('Pay in 0, 6 or 12 month installment: '))
        if month == 0:
           print ('Please pay ${:,.2f}. No installment plan.'.format(cost))
        elif month == 6:
            interest = cost *0.05
            installment = (cost + interest) / month
            print('{} month installment plan of ${:,.2f} per month'.format(month, installment))
        elif month == 12:
            interest = cost *0.1
            installment = (cost + interest) / month
            print('{} month installment plan of ${:,.2f} per month'.format(month, installment))
        else:
            print("Invalid month selection")

lab2_q11()