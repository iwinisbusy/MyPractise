#int is whole number
#float number with decimal
#str is alphabet or character

from timeit import repeat


def main(): #This is like button option
    print("\nHello World:")
    print("\nT06")
    print("Awesome!\n") # \n is to give a paragraph

def play():
    print("Yes")
    print(2+3) #this will be calculated out in the output
    print("2+3 =", 2+3)
    print("\n\n")

def cal():
    print("Hello world", end = "*")
    print(2+3, end= "*")
    print("2+3 =", 2+3)
    print("\n\n")
    print("a", "b", 5, 6, "\t", 7) # "\t" is to make a big space between word in a line just like TAB fucntion in your keyboard
    print("\n\n\n")

def score():
    player_name = "Bob" # Try to use lower case for variable, Variable is case sensitive, Var also cannot start with number
    goal_score = 3
    print(player_name, "Scored", goal_score+1, "Points")
    print("\n\n\n")

def birth():
    birthyear = 2000
    age = 2019 - birthyear
    print(age)

def temp():
    f = float(input("Enter your Farenheight value:"))
    c = 5/9*(f-32)
    print("Fahrenheit to centigrate is = ", int(c))
    print("\n\n")

def inputtest():
    name = input("Enter friends name: ") #input will be in str in default
    print(name)
    print(type(name))

    age = int(input("Enter friends age: "))
    print("Age is", age)
    print("You are born in", 2022 - age, "year")
    print(type(age))

def remaindertest():
    print("\n")
    print(5%2) #this will show remainder
    print(5/2) #this will show the calculated one 
    print("\n")

def testt():
    # alignment formatting
    print("I am {:<15s} left".format("ALIGN"))
    print("I am {:>15s} right".format("ALIGN"))
    print("I am {:^15s} center".format("ALIGN"))


    # number formatting with alignment and thousand separater
    text1 = "I am ${:<10,.2f} left".format(1254.6587)
    text2 = "I am ${:>10,.2f} right".format(1254.6387)
    text3 = "I am ${:^10,.2f} center".format(1254.6487)
    print(text1)
    print(text2)
    print(text3)

def slicingDemo():
     # Slicing: [<start>:<end>:<increment>]
    name="AliBaBa"
    #     0123456  len = 7

    # from pos 0 to 5, EXCLUDING pos 6, increment default to 1
    print("name[0:6] -->", name[0:6])

    # from pos 0 to 5, EXCLUDING pos 6, increment default to 1
    print("name[:6] -->", name[:6])

    # from pos 0 to 2, EXCLUDING pos 3, increment default to 1
    print("name[0:3] -->", name[0:3])

    # from pos 4 to 6, EXCLUDING pos 7, increment default to 1
    print("name[4:7] -->", name[4:7])

    # from pos 4 to end, increment default to 1
    print("name[4:] -->", name[4:])

    # from pos 0 to 5, EXCLUDING pos 6, increment 2
    print("name[0:6:2] -->", name[0:6:2])

    # from pos 5 to 0, EXCLUDING pos 0, decrement -2
    print("name[5:0:-2] -->", name[5:0:-2])

    # reverse
    print("name[::-1] -->", name[::-1])

    print(name*3)

def stringSplit():
    text = input("Enter name separated by <space>: ")
    firstname, lastname = text.split(" ")
    print(firstname.strip())
    print(lastname.strip())
   
    names = input("Enter name separated by <space>: ").split(" ")
    print(names)
    print(names[0].strip())
    print(names[1].strip())

def stringMethodsDemo():
    # list of String methods to try
    name = "Ali BaBa"
    print( "capitalize name =", name.capitalize() )
    print( "upper name =", name.upper() )
    print( "lower name =", name.lower() )
    print( "title name =", name.title() )
    print( "This is |", name.center(15), "| centered" )
    print( "This is |", name.rjust(15), "| right-justified" )
    print( "This is |", name.ljust(15), "| left-justified" )
    print( "No of <b> =", name.count('b') )
    print( "No of <Ba> =", name.count('Ba') )
    print( "B is located at position", name.find('B') )
    print( "B right-most position is", name.rfind('B') )
    print( "Replacing <Ba> with <Ca> =", name.replace("Ba", "Ca") )
    print("name is still", name)
    name = name.replace("Ba", "Ca")
    print(name)

def stringFormatting():
    # alignment formatting
    value = "ALIGN"
    text1 = "I am {:<10s} left".format(value)
    text2 = "I am {:>10s} right".format(value)
    text3 = "I am {:^10s} center".format(value)
    print(text1)
    print(text2)
    print(text3)

    # number formatting with alignment
    value = 1254.6587
    print("I am {:<10.2f} left".format(value))
    print("I am {:>10.2f} right".format(value))
    print("I am {:^10.2f} center".format(value))

    # padding with 0
    print("I am {:<010.2f} left".format(value))
    print("I am {:>010.2f} right".format(value))
    print("I am {:^010.2f} center".format(value))

    # number formatting with alignment, with thousand separator
    print("I am {:<10,.2f} left".format(value))
    print("I am {:>10,.2f} right".format(value))
    print("I am {:^10,.2f} center".format(value))

    # number formatting with alignment, with $ and thousand separator
    value = 12546587
    print("I am ${:<15,d} left".format(value))
    print("I am ${:>15,d} right".format(value))
    print("I am ${:^15,d} center".format(value))

    totalAmount = 12345.678
    print("Total amount: ${:>10.2f} only".format(totalAmount))
    # > for right align
    # 10 define the width
    # .2f define 2 decimal spaces

def fStringFormatting():
    # alignment formatting
    value = "ALIGN"
    text1 = f"I am {value:<10s} left"
    text2 = f"I am {value:>10s} right"
    text3 = f"I am {value:^10s} center"
    print(text1)
    print(text2)
    print(text3)

    # number formatting with alignment
    value = 1254.6587
    print(f"I am {value:<10.2f} left")
    print(f"I am {value:>10.2f} right")
    print(f"I am {value:^10.2f} center")

    # padding with 0
    print(f"I am {value:<010.2f} left")
    print(f"I am {value:>010.2f} right")
    print(f"I am {value:^010.2f} center")

    # number formatting with alignment, with thousand separator
    print(f"I am {value:<10,.2f} left")
    print(f"I am {value:>10,.2f} right")
    print(f"I am {value:^10,.2f} center")

    # number formatting with alignment, with $ and thousand separator
    value = 12546587
    print(f"I am ${value:<15,d} left")
    print(f"I am ${value:>15,d} right")
    print(f"I am ${value:^15,d} center")

    totalAmount = 12345.678
    print(f"Total amount: ${totalAmount:>10,.2f} only")
    # > for right align
    # 10 define the width
    # .2f define 2 decimal spaces

def sem2_review():
    # handling inputs 
    height = float(input("Enter height in meters(decimals): "))
    weight = float(input("Enter weight in kg: "))

    # processing - use of assignment, operators
    bmi = weight / (height * height)

    # output BMI and catergory 
    print("Your BMI is {:.1f}".format(bmi), end="")

    if bmi >= 30:
        print("and you are Obese")
    elif bmi >= 25:
        print("and you are Overweight")
    elif bmi >= 18.5:
        print("and you are Healthy")
    else:  # < 18.5
        print("and you are Underweight")

def sem2_1():
    numb1 = int(input("Enter First number: "))
    numb2 = int(input("Enter Second number: " ))
    

    if numb1 > numb2:
        total = 0
        for i in range(numb1, numb2+1):
            print(i)
            total = total + i
        print(total)
    else:
        total = 0
        for i in range(numb1, numb2-1, -1):
            print(i)
            total = total + i
        print(total)
    
def aforloop():
   
    numberstring = input("Enter 3 Digit Number: ")
    total = 0
    for char in numberstring:
        total = total + int(char)
 
    print("Sum =", total)
    
def bforloop():
    word = str(input("Enter a Word:"))
    num_times = int(input("Enter the number of times:"))
    for i in range (num_times):
        print (word)

from random import randint

def guessingGame():
    diceValue = randint(1, 6)
    tries = 1
    while tries <= 3:
        guess = int(input("Try {}. Enter guess: ".format(tries)))
        if diceValue == guess:
            print("You got it!")
            break

        print("Incorrect")
        tries += 1

    if tries > 3:
        print("Sorry, value is {}".format(diceValue))

def guessingMain():
    while True:
        guessingGame()  # play one game
        playAgain = input("Continue? y/n: ")
        if playAgain[0] in "Nn":
            break


def whileSamples():
    # while example 1
    stop = input("(R)epeat or (S)top : ")
    while stop[0] not in "Ss":
        print("ok, let's repeat one more time")
        stop = input("(R)epeat or (S)top : ")

    print("Done#1 !!")

    # while example 2
    while True:
        stop = input("(R)epeat or (S)top : ")
        if stop[0] in "Ss":
            break
        
        print("ok, let's repeat one more time")

    print("Done#2 !!")

#guessingGame()
#bforloop()
#sem2_1()
#main() # Here i push the button option 'main' to print Hello world
#play() # Here i push button option 'play'cal() # Here i want cal(): option to run
#score()# Here i want score(): to run
#birth()
#remaindertest()
#temp()
#inputtest()
#testt()

