price = float(input("Price of purchased property: "))
if price > 180000 and price < 360000:
    tax = 0.01*180000
    print("Interest is: ", tax)
    totalprice = price + tax
    print("Total price is: ", totalprice)

if price > 360000:
    