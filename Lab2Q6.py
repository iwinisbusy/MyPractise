"""
Write a program that determines whether two integers are even or odd. Display one of the following messages:
- “The 2 numbers are even”
- “The 2 numbers are odd”
- “One number is even and the other is odd”
"""
def lab2_q6():
    n1 = int(input("Enter 1st no: "))
    n2 = int(input("Enter 2nd no: "))
    # check if numbers are both odd or even
    # or one odd one even
    test = n1%2 + n2%2

    if test == 0:
        print("The 2 numbers are even")
    elif test == 2:
        print("The 2 numbers are odd")
    else:
        print("One number is even and the other is odd")

    if n1 % 2 == 0:    # is num1 even??
        if n2 % 2 == 0:  # is num2 even??
            print("The 2 numbers are even")
        else:
            print("One number is even and the other is odd")
    else:                   # num1 is odd
        if n2 % 2 != 0:
            print("The 2 numbers are odd")
        else:
            print("One number is even and the other is odd")

    # using logical operator and
    if n1%2==0 and n2%2==0:
        print("The 2 numbers are even")
    elif n1%2!=0 and n2%2!=0:
        print("The 2 numbers are odd")
    else:
        print("one number is even and the other is odd")

    if n1%2 == 0:
        if n2%2 == 0:
            print("The 2 numbers are even")
        else:
            print("One number is even and the other is odd")
    #else
    if n1%2 != 0:
        if n2%2 != 0:
            print("The 2 numbers are not even")
        else:
            print("One number is even and the other is odd")




lab2_q6()