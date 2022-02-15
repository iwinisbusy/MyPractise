def sumSquares(num):
    sumOfSquares = 0
    # 1**2  2**2  3**2   4**2
    # 1*1    2*2  3*3    4*4
    for i in range(1, num+1):
        sumOfSquares = sumOfSquares + i*i
    
    return sumOfSquares

def main():
    num = int(input("Enter a number: "))
    result = sumSquares(num)
    print("Sum of squares for {} = {}".format(num, result))

main()