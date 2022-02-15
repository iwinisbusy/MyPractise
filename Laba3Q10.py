def divide(x, y):
    quotient = 0
    while x >= y:
        x = x - y
        quotient += 1

    return quotient, x

#   x    y         quotient    
#   11   4     7   1
#   7    4     3   2
#   3    4  STOP   x become remainder

def main():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    quotient, remainder = divide(num1, num2)
    print(quotient, remainder)

main()