def lab3Q1a():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    for i in range(num1, num2+1):         # 1 2 3 4 5
        print(i)

def lab3Q1b():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    total = 0
    for i in range(num1, num2+1):         # 1 2 3 4 5
        print(i)
        total = total + i
    
    print(total)

def lab3Q2a():
    word = str(input("Enter a Word:"))
    num_times = int(input("Enter the number of times:"))
    for i in range (num_times):
        print (word)

def lab3q2b():
    #input
    strinput = str(input("Input string:"))
    rep = int(len(strinput))
    #processing and output
    for i in range(0, rep+1):
        print(strinput[0:i])

def lab3Q2c():
    word = input("Enter a Word:")
    num_times = int(input("Enter the number of times:"))
    for i in range(num_times):
        print(word)

    # while example 2
    while True:
        stop = input("(R)epeat or (S)top : ")
        if stop[0] in "Ss":
            break
        
        print("ok, let's repeat one more time")

    while True:
        word = input("Input string: ")
        if word.lower() == 'exit':
            break

        number = int(input("Number of times to repeat: "))
        for i in range(number):
            print(word)

    print('end')