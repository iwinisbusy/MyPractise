"""
10. Write a triangle checker program that reads in the 3 sides of a triangle. The program checks whether the 3 values can form a triangle. A triangle will not be possible if the sum of any two is less than or equal to the third. If the values can form a triangle, print the type of triangle according to the table below.

All 3 sides are equal   -> equilateral
Any two sides are equal -> isosceles
All 3 are unequal       -> scalene
"""
def lab2_q10():
    sideA = float(input('Enter 1st side of triangle: '))
    sideB = float(input('Enter 2nd side of triangle: '))
    sideC = float(input('Enter 3rd side of triangle: '))
    # checks whether the 3 values can form a triangle
    if (sideA + sideB <= sideC) or (sideA + sideC <= sideB) or (sideC + sideB <= sideA):
        print("This is not a triangle")
    else:
        if sideA == sideB == sideC:
            print("All 3 sides are equal -> equilateral")
        elif sideA == sideB or sideB == sideC or sideC == sideA:
            print("Any two sides are equal -> isosceles")
        else:
            print("All 3 are unequal -> scalene")


lab2_q10()
