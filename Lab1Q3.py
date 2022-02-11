def q3():
    input1 = (int(input("Enter 1st Number: ")))
    input2 = (int(input("Enter 2nd Number: ")))
    input3 = (int(input("Enter 3rd Number: ")))
    sum1 = (input1 + input2 + input3)
    product1 = (input1 * input2 * input3)
    average1 = float((sum1/3))
    print("\n The sum of all input is: ", sum1)
    print("\n Product of the 3 input is: ", product1)
    print("\n", "The average of 3 input is: ", average1, "\n")

q3()

def q3lec():
    # Input: reading in the integer nubmber
    number = int(input("Enter 3 Digit Number: "))  # number = 345
    # Processing: using operators to extract each digit
    digit1 = number // 100   # 3
    digit2 = number // 10 % 10 # ==> 34 % 10 = 4
    digit3 = number % 10    # 5
    #print(digit1, " - ", digit2, " - ", digit3 )
    # Processing: compute total and product
    total = digit1 + digit2 + digit3
    product = digit1 * digit2 * digit3
    # Output: print the total and product
    print("Sum =", total)
    print("Product =", product)

q3lec()