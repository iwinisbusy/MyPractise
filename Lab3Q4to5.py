def lab3Q5():
    # display of menu, getting option and decision flow
    while True:
        print("Menu")
        print("1. Action A")
        print("2. Aciton B")
        print("3. Action C")
        print("0. Quit")
        option = int(input("Enter choice: ")
        if option == 0:
            break
        elif option == 1:
            actionA()
        elif option == 2:
            actionB()
        else:
            actionC()    


def lab3Q4():
    
    totalPrice = 0
    while True:
        quantity = int(input("Enter quantity: "))

        if quantity == -1:
            break

        unitPrice = float(input("Enter unit Price: "))
        subTotal = quantity * unitPrice
        totalPrice = totalPrice + subTotal
        print("Subtotal is ${:.2f}".format(subTotal))

    print("Total price is ${:.2f}".format(totalPrice))
    gst = totalPrice * 0.07
    print("GST is ${:.2f}".format(gst))
    print("Please pay ${:.2f}".format(totalPrice + gst))
