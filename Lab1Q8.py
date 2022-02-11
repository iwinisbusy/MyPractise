def lab1_q8():
    # Input the loan amount, interest and duration
    loanAmount = float(input("Enter loan amount: "))
    duration = int(input("Enter load duration: "))
    interestRate = float(input("Enter interest rate: "))

    # compute the compound Interest 
    compundInterest = loanAmount * ( 1 + interestRate/100) ** duration

    # dusplay the result
    print("Loan with compund interest after {} years: ${:>10,.2f}".format(duration, compundInterest))

lab1_q8()
