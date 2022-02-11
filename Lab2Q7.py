"""
7. Singapore NRIC numbers have the following format #0000000@, where
- length of the NRIC is 9
- # is a letter that can be "S", "T", "F" or "G"
- followed by 7 digits
- @ is any reference letter A to Z or a to z

Write a program that inputs a NRIC number and displays whether a NRIC is valid. Display “Valid NRIC” or, if it is invalid, one of the following error messages:
  - Length must be exactly 9
  - The first letter must be S, T, F or G
  - Must consist of 7 digits
  - Reference letter must be A to Z or a to z
                                 ^^^^^^^
Example                         012345678   nric[1:8]  # exclude pos 8
            Run 1   Enter NRIC: S1234567A
                    Valid NRIC

            Run 2   Enter NRIC: X123456789B
                    Length must be exactly 9

            Run 3   Enter NRIC: S12345XXB
                    Must consist of 7 digits
"""
def lab2_q7():
    # get nric input and remove all front and back spaces
    nric = input("Enter NRIC : ").strip()
    nric = nric.upper()   # convert all to uppercase     

    if len(nric) == 9:
        if nric[0] in "STFG":
            if nric[1:8].isdigit():  
                if nric[-1].isalpha():
                    print("Valid NRIC")
                else:
                    print("Reference letter must be A to Z or a to z")
            else:
                print("Must consist of 7 digits")
        else:
            print("The first letter must be S, T, F or G")
    else:
        print("Length must be exactly 9")

lab2_q7()