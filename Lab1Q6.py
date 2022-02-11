def lab1_q6():
    #input
    mealAmount = float(input("Enter the meal amount:$ "))

    #process
    discountAmount = mealAmount * 0.5
    serviceCharge = discountAmount * 0.1
    gstCharge = (discountAmount + serviceCharge) * 0.07
    totalAmount = discountAmount + serviceCharge + gstCharge

    text1 = "Cost of meal:    ${:>10,.2f} ".format(mealAmount)
    text2 = "50% Discount:    ${:>10,.2f} ".format(discountAmount)
    text3 = "Service Charge:  ${:>10,.2f} ".format(serviceCharge)
    text4 = "GST Charge:      ${:>10,.2f} ".format(gstCharge)
    text5 = "Total Amount:    ${:>10,.2f} ".format(totalAmount)
    print(text1)
    print(text2)
    print(text3)
    print(text4)
    print(text5)

lab1_q6()