import math

def lab1_q7():
    #Input: th 3 sides of triangle (float)
    a = float(input("Input length of side a: "))  #1
    b = float(input("Input length of side b: "))  #1
    c = float(input("Input length of side c: "))  #9
    #processing: compute semi-perimeter, compute area
    s = 0.5 * (a+b+c)
    area = math.sqrt( s*(s-a)*(s-b)*(s-c))
    #Output: display area
    print("Tha area of the triangle is {:.2f}".format(area))

lab1_q7()