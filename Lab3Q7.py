def displayFromTo(x, y):
    for i in range(x, y+1):         # 1 2 3 4 5
        print(i)

def main():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    displayFromTo(num1, num2)

main()