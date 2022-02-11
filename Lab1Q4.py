def q4():
    # Input: positive integer representing seconds
    input1 = int(input("Enter seconds in integer: "))

    # Processing: computations to convert into hrs, mins and secs
    hours = input1//3600 % 24
    minutes = input1//60%60
    seconds = input1%60

    # Output: display the result (hours, minutes and seconds)
    print(hours, "hr", minutes, "min", seconds, "sec")
    print("\n")
    print("{} hr {} min {} sec".format(hours, minutes, seconds))
    print("\n")
    
q4()